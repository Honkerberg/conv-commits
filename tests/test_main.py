import unittest

from main import new_function, compute_sum


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(new_function(), "Hello World!")

    def test_compute_sum(self):
        self.assertEqual(compute_sum(10, 20), 30)

if __name__ == '__main__':
    unittest.main()