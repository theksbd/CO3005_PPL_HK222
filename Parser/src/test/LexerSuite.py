import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test1(self):
        """test simple string"""
        self.assertTrue(TestLexer.test(
            "duy.tran2903", "duy.tran2903,<EOF>", 101))

    def test2(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(
            "duy2.tran2903", "duy.tran.3_12,<EOF>", 102))
