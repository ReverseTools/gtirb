import unittest
from gtirb.serialization import Serialization, TypeNameHintError


class TestSerialization(unittest.TestCase):
    def test_parse_type(self):
        def test_positive(type_name, oracle):
            self.assertEqual(Serialization.parse_type(type_name), oracle)
        positive_tests = [
            ('mapping', ('mapping', ())),
            ('mapping<FOO,BAR>',
             ('mapping', (('FOO', ()), ('BAR', ())))),
            ('mapping<FOO,set<BAR>>',
             ('mapping', (('FOO', ()), ('set', (('BAR', ()),))))),
            ('mapping<FOO,mapping<BAR,BAZ>>',
             ('mapping', (('FOO', ()),
                          ('mapping', (('BAR', ()), ('BAZ', ())))))),
            ('mapping<mapping<BAR,BAZ>,FOO>',
             ('mapping', (('mapping', (('BAR', ()), ('BAZ', ()))),
                          ('FOO', ())))),
        ]
        for type_name, oracle in positive_tests:
            test_positive(type_name, oracle)

        def test_negative(type_name):
            with self.assertRaises(TypeNameHintError, msg=type_name):
                Serialization.parse_type(type_name)

        negative_tests = [
            'mapping<<>',
            'mapping<>>',
            'mapping<><>',
            'mapping<<><>>',
            'mapping<<foo><bar>>',
        ]
        for type_name in negative_tests:
            test_negative(type_name)

    def test_type_tree_str(self):
        def test_one(type_tree, oracle):
            self.assertEqual(Serialization.type_tree_str(type_tree), oracle)
        """The inverse transformation of the above tests"""
        positive_tests = [
            ('mapping', ('mapping', ())),
            ('mapping<FOO,BAR>',
             ('mapping', (('FOO', ()), ('BAR', ())))),
            ('mapping<FOO,set<BAR>>',
             ('mapping', (('FOO', ()), ('set', (('BAR', ()),))))),
            ('mapping<FOO,mapping<BAR,BAZ>>',
             ('mapping', (('FOO', ()),
                          ('mapping', (('BAR', ()), ('BAZ', ())))))),
            ('mapping<mapping<BAR,BAZ>,FOO>',
             ('mapping', (('mapping', (('BAR', ()), ('BAZ', ()))),
                          ('FOO', ())))),
        ]
        for oracle, type_tree in positive_tests:
            test_one(type_tree, oracle)


if __name__ == '__main__':
    unittest.main()