import unittest

import main


class MedianFinderTest(unittest.TestCase):

    def test_raise_error_when_no_values(self):
        with self.assertRaises(RuntimeError):
            main.MedianFinder().get()

    def test_get_when_one_value_provided(self):
        finder = main.MedianFinder()
        finder.add(4)

        median = finder.get()

        self.assertEqual(4, median)

    def test_get_with_odd_number_of_values(self):
        finder = main.MedianFinder()
        for n in (6, 3, 4):
            finder.add(n)

        median = finder.get()

        self.assertEqual(4, median)

    def test_get_with_even_number_of_values(self):
        finder = main.MedianFinder()
        for n in (6, 3, 4, 10):
            finder.add(n)

        median = finder.get()

        self.assertEqual(5, median)


if __name__ == "__main__":
    unittest.main()
