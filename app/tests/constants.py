"""
declaring different scenarious for tests and static data for tests
"""
# import constants
from google_drive_api.constants import (
    TOO_LARGE_FILE,
    NOT_VALID_TYPE_ERROR
)

# emptry values for params
EMPTY_NAME = ""

# wrong symbols in name
WRONG_NAME_FORMAT = "song_/\file.mp3" # yeah, we can create by Python
                                      # mp3 file by writing text


EMPTY_NAME_FIELD_ERROR = {'name': ['This field may not be blank.']}
NOT_VALID_TYPE_ERROR_JSON = {
    'detail': ["File couldn't be converted. Maybe, it has wrong symbols in name. Server is waiting only text-format file."],
    'code': ['NOT_VALID_TYPE_ERROR']
}

# it's not enough, of course (:
MAKE_REQUEST_SCENARIOS = [
    # wrong fields scenarious
    {
        "wrong_raw": {
            "name": "name",
            "data": [EMPTY_NAME]
        },
        "error_json": EMPTY_NAME_FIELD_ERROR
    },
    {
        "wrong_raw": {
            "name": "name",
            "data": [WRONG_NAME_FORMAT]
        },
        "error_json": NOT_VALID_TYPE_ERROR_JSON
    },    

]