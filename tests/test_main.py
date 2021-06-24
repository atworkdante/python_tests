import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        """Um teste de sucesso"""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """Um teste de meio sucesso"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
