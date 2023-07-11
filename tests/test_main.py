import unittest

from main import new_function


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(new_function(), "Hello World!")

if __name__ == '__main__':
    unittest.main()