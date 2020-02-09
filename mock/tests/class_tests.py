from io import StringIO
from unittest.mock import patch
import unittest
from classes import Worker, Helper


class ClassesTests(unittest.TestCase):


    def test_must_return_expected_work_value(self):
        with patch('classes.Helper', autospec=True) as HelperMock:
            worker = Worker()
            HelperMock.assert_called_once_with('db')

            HelperMock.return_value.get_path.return_value = 'test_path'

            return_value = worker.work()
            expected = 'test_path'
            self.assertEqual(expected, return_value)

    def test_must_return_expected_work_value_using_patch_object(self):
        with patch.object(Helper, 'get_path', return_value='test_path', autospec=True) as GetPathMock:
            worker = Worker()

            return_value = worker.work()

            GetPathMock.assert_called_once()
            expected = 'test_path'
            self.assertEqual(expected, return_value)

    def test_must_call_print_with_right_arg(self):
        with patch('classes.print') as PrintMock:
            with patch('os.getcwd', return_value='/home/'):
                with patch.dict('os.environ', {'MY_VAR': 'testing'}):
                    worker = Worker()

                    actual_return = worker.work_on_env()
                    expected = '/home/testing'
                    self.assertEqual(expected, actual_return)

                    PrintMock.assert_called_once_with(f'Working on {expected}')

    def test_context_manager(self):
        with patch('classes.open') as mock_open:
            worker = Worker()

            mock_open.return_value.__enter__.return_value = StringIO('testing')
            self.assertEqual(worker.size_of(), 7)

    def test_must_use_percentage_and_calculate(self):
        with patch.object(Worker, 'PERCENTAGE', 0.5):
            worker = Worker

            actual_return = worker.calculate(worker, 5)
            expected = 2.5

            self.assertEqual(actual_return, expected)
