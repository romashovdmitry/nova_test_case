# Python imports
import os

# Google API library imports
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# import custom foos, classes and logger
from main.utils import foo_name
from main.settings import logger


async def remove_file(file: str) -> None:
    """
    Remove file from project. 
    Parameters:
        file: path of file that would be deleted
    """
    os.remove(file)


async def google_drive_post_request(
        name: str
) -> (bool, str | None):
    """
    Foo make post request to Google Drive API.
    Additional links:
    How to: https://dev.to/binaryibex/python-and-google-drive-how-to-list-and-create-files-and-folders-2023-2nmm
    About Credentials: https://stackoverflow.com/a/47337595
    Parameters:
        name: file name, that we would create on Google Drive Disc
        data: text of file, that we would create
    Returns:
        bool: succes or not request to API Google Drive
        str | None: text of exception of there is exception
            or None if success
    """
    try:
        credentials = service_account.Credentials.from_service_account_file(
                os.getcwd() + '/credentials.json', scopes=['https://www.googleapis.com/auth/drive']
            )
        service = build("drive", "v3", credentials=credentials)
        file_metadata = {
            'name': name,
            'parents': [os.getenv("GOOGLE_DRIVE_DIRECTORY_ID")]
        }
        media = MediaFileUpload(name)
        file = service.files().create(body=file_metadata, media_body=media).execute()
        await remove_file(file)

        return True, None

    except Exception as ex:
        logger.error(
            f'[{foo_name()}]'
            f'Ex text: {str(ex)}'
        )

        return False, str(ex)
