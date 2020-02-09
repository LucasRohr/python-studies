from unittest.mock import Mock


def get_mocked_response():
    response_return = {
        'content': [1, 2, 3]
    }
    response = Mock(**{
        'json.return_value': response_return,
        'status_code': 200
    })

    return response
