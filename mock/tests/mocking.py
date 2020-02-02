import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock, patch
from functions import get_thing, requests
import functions


def get_mocked_response():
    response_return = {
        'content': [1, 2, 3]
    }
    response = Mock(**{
        'json.return_value': response_return,
        'status_code': 200
    })

    return response


class TestGet(unittest.TestCase):

    # using autospec=True to match mocked object interface
    # same thing as: Mock(spec=object) or Mock(spec=['method_one', 'method_two'])

    # using patch as a decorator
    # patching all of requests = @patch('functions.requests')
    # patching just the 'get' method with .object()
    @patch.object(requests, 'get', side_effect=[Timeout, get_mocked_response()], autospec=True)
    def test_get_thing_timeout(self, requests_mock):
        # === because of patch.object, these lines are now unnecessary ===
        # response = get_mocked_response()
        # requests_mock.get.side_effect = [Timeout, response]
        requests_mock.return_value = get_mocked_response()

        with self.assertRaises(Timeout):
            get_thing()

        result = get_thing()
        expected = [1, 2, 3]
        self.assertEqual(expected, result['content'])

    # using patch as a context manager

    def test_get_thing_status_ok(self):
        with patch(f'{functions}.requests', autospec=True) as requests_mock:
            requests_mock.get.return_value = get_mocked_response()
            result = get_thing()
            path = 'http://localhost/api/get'
            requests_mock.get.assert_called_once_with(path)

            expected = [1, 2, 3]
            self.assertEqual(expected, result['content'])


if __name__ == '__main__':
    unittest.main()
