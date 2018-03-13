import unittest

class TestPythonMethods(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(5 + 3, 8)

if __name__ == '__main__':
    unittest.main()
