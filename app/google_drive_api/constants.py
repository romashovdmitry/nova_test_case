""" Module with static data, exceptions texts, etc similar """

NOT_VALID_TYPE_ERROR = {
    "detail": (
        "File couldn't be converted. "
        "Maybe, it has wrong symbols in name. "
        "Server is waiting only text-format file."
    ),
    'code': "NOT_VALID_TYPE_ERROR"
}

GOOGLE_DRIVE_API_DENY_REQUEST = {
    "detail": "File is not created, Google Drive API deny request",
    'code': "FILE_NOT_CREATED"
}


FILE_SIZE_LIMIT = 5 * 1024 * 1024
TOO_LARGE_FILE = {
    "detail": "File is too large to be processed",
    'code': "GOOGLE_DRIVE_API_SIZE_LIMIT"
}

