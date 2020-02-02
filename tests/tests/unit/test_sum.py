import unittest
from modules import sum_list


class SumTest(unittest.TestCase):

    def test_must_sum_integers_list_correctly(self):
        int_list = [4, 5, 6]

        result = sum_list.make_sum(int_list)

        self.assertEqual(result, 15)

    def test_must_raise_error_on_wrong_list_sum(self):
        int_list = [4, 5, 6]

        result = sum_list.make_sum(int_list)

        with self.assertRaises(AssertionError):
            self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()
