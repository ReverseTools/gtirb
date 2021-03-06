"""The IR is the core class for reading and writing GTIRB files.

    You can open a GTIRB Protobuf file and load it into an IR instance:

    >>> ir = IR.load_protobuf('filename.gtirb')

    And then you can write the IR instance as a Protobuf file:

    >>> ir.save_protobuf('filename.gtirb')
"""

import IR_pb2
import typing
from uuid import UUID

from .auxdata import AuxData, AuxDataContainer
from .module import Module
from .util import DictLike


class IR(AuxDataContainer):
    """A complete internal representation consisting of multiple Modules.

    :ivar modules: A list of Modules contained in the IR.
    """

    def __init__(
        self,
        modules=list(),  # type: typing.Iterable[Module]
        aux_data=dict(),  # type: DictLike[str, AuxData]
        uuid=None,  # type: typing.Optional[UUID]
    ):
        # type: (...) -> None
        """
        :param modules: A list of Modules contained in the IR.
        :param aux_data: The initial auxiliary data to be associated
            with the object, as a mapping from names to
            :class:`gtirb.AuxData`. Defaults to an empty :class:`dict`
        :param uuid: The UUID of this ``IR``,
            or None if a new UUID needs generated via :func:`uuid.uuid4`.
            Defaults to None.
        """

        # Modules are decoded before the aux data, since the UUID decoder
        # checks Node's cache.
        self.modules = list(modules)  # type: typing.List[Module]
        super().__init__(aux_data, uuid)

    @classmethod
    def _decode_protobuf(cls, proto_ir, uuid):
        # type: (IR_pb2.IR, UUID) -> IR
        aux_data = (
            (key, AuxData._from_protobuf(val))
            for key, val in proto_ir.aux_data_container.aux_data.items()
        )
        modules = (Module._from_protobuf(m) for m in proto_ir.modules)
        return cls(modules, aux_data, uuid)

    def _to_protobuf(self):
        # type: () -> IR_pb2.IR
        proto_ir = IR_pb2.IR()
        proto_ir.uuid = self.uuid.bytes
        proto_ir.modules.extend(m._to_protobuf() for m in self.modules)
        proto_ir.aux_data_container.CopyFrom(super()._to_protobuf())
        return proto_ir

    def deep_eq(self, other):
        # type: (typing.Any) -> bool
        # Do not move __eq__. See docstring for Node.deep_eq for more info.
        if not isinstance(other, IR) or not super().deep_eq(other):
            return False
        self_modules = sorted(self.modules, key=lambda m: m.uuid)
        other_modules = sorted(other.modules, key=lambda m: m.uuid)
        if not len(self_modules) == len(other_modules):
            return False
        for self_module, other_module in zip(self_modules, other_modules):
            if not self_module.deep_eq(other_module):
                return False
        return True

    @staticmethod
    def load_protobuf_file(protobuf_file):
        # type: (typing.BinaryIO) -> IR
        """Load IR from a Protobuf object.

        Use this function when you have a Protobuf object already loaded,
        and you want to parse it as a GTIRB IR.
        If the Protobuf object is stored in a file,
        use :func:`gtirb.IR.load_protobuf` instead.

        :param protobuf_file: A byte stream encoding a GTIRB Protobuf message.
        :returns: An IR object representing the same
            information that is contained in ``protobuf_file``.
        """

        ir = IR_pb2.IR()
        ir.ParseFromString(protobuf_file.read())
        return IR._from_protobuf(ir)

    @staticmethod
    def load_protobuf(file_name):
        # type: (str) -> IR
        """Load IR from a Protobuf file at the specified path.

        :param file_name: The path to the Protobuf file.
        :returns: A Python GTIRB IR object.
        """
        with open(file_name, "rb") as f:
            return IR.load_protobuf_file(f)

    def save_protobuf_file(self, protobuf_file):
        # type: (typing.BinaryIO) -> None
        """Save ``self`` to a Protobuf object.

        :param protobuf_file: The byte stream to write the GTIRB Protobuf
            message to.
        """

        protobuf_file.write(self._to_protobuf().SerializeToString())

    def save_protobuf(self, file_name):
        # type: (str) -> None
        """Save ``self`` to a Protobuf file at the specified path.

        :param file_name: The file path at which to
            save the Protobuf representation of ``self``.
        """
        with open(file_name, "wb") as f:
            self.save_protobuf_file(f)

    def __repr__(self):
        # type: () -> str
        return (
            "IR("
            "uuid={uuid!r}, "
            "modules={modules!r}, "
            ")".format(**self.__dict__)
        )
