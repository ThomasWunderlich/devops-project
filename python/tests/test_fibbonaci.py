import unittest
from fib.main import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), [])

    def test_fibonacci_negative(self):
        # This should throw an exception
        self.assertRaises(Exception, fibonacci, -1)

    def test_fibonacci_valid_sequence(self):
        fib_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]
        self.assertEqual(fibonacci(29), fib_seq)



if __name__ == '__main__':
    unittest.main()
