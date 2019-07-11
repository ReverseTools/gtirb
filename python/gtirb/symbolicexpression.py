from uuid import UUID

import SymbolicExpression_pb2


class SymAddrAddr:
    """
    Represents a "symbolic operand" of the form
    "(Sym1 - Sym2) / Scale + Offset"
    """

    def __init__(self, scale, offset, symbol1, symbol2):
        self.scale = scale
        self.offset = offset
        self.symbol1 = symbol1
        self.symbol2 = symbol2

    def _to_protobuf(self):
        """
        Returns protobuf representation of the object

        :returns: protobuf representation of the object
        :rtype: protobuf object

        """
        ret = SymbolicExpression_pb2.SymAddrAddr()
        ret.scale = self.scale
        ret.offset = self.offset
        ret.symbol1_uuid = self.symbol1.uuid.bytes
        ret.symbol2_uuid = self.symbol2.uuid.bytes
        return ret

    @classmethod
    def _from_protobuf(cls, sym_addr_addr, uuid_cache=None):
        """
        Load this cls from protobuf object
        """
        symbol1_uuid = UUID(bytes=sym_addr_addr.symbol1_uuid)
        symbol2_uuid = UUID(bytes=sym_addr_addr.symbol2_uuid)
        symbol1 = None
        symbol2 = None
        if uuid_cache is not None:
            symbol1 = uuid_cache.get(symbol1_uuid)
            symbol2 = uuid_cache.get(symbol2_uuid)
        return cls(sym_addr_addr.scale, sym_addr_addr.offset, symbol1, symbol2)


class SymAddrConst:
    """
    Represents a "symbolic operand" of the form "Sym + Offset".
    """
    def __init__(self, offset, symbol):
        self.offset = offset
        self.symbol = symbol

    def _to_protobuf(self):
        """
        Returns protobuf representation of the object

        :returns: protobuf representation of the object
        :rtype: protobuf object

        """
        ret = SymbolicExpression_pb2.SymAddrConst()
        ret.offset = self.offset
        if self.symbol is not None:
            ret.symbol_uuid = self.symbol.uuid.bytes
        return ret

    @classmethod
    def _from_protobuf(cls, sym_addr_const, uuid_cache=None):
        """
        Load this cls from protobuf object
        """
        symbol_uuid = UUID(bytes=sym_addr_const.symbol_uuid)
        symbol = None
        if uuid_cache is not None:
            symbol = uuid_cache.get(symbol_uuid)
        return cls(sym_addr_const.offset, symbol)


class SymStackConst:
    """
    Represents a "symbolic operand" of the form "Sym + Offset",
    representing an offset from a stack variable.
    """
    def __init__(self, offset, symbol):
        self.offset = offset
        self.symbol = symbol

    def _to_protobuf(self):
        """
        Returns protobuf representation of the object

        :returns: protobuf representation of the object
        :rtype: protobuf object

        """
        ret = SymbolicExpression_pb2.SymStackConst()
        ret.offset = self.offset
        if self.symbol is not None:
            ret.symbol_uuid = self.symbol.uuid.bytes
        return ret

    @classmethod
    def _from_protobuf(cls, sym_stack_const, uuid_cache=None):
        """
        Load this cls from protobuf object
        """
        symbol_uuid = UUID(bytes=sym_stack_const.symbol_uuid)
        symbol = None
        if uuid_cache is not None:
            symbol = uuid_cache.get(symbol_uuid)
        return cls(sym_stack_const.offset, symbol)
