""" Api transactions to Google Drive API """
# Python imports
import os

# Google API library imports
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# import custom foos, classes and logger
from main.utils import foo_name, remove_file
from main.settings import logger


async def check_file_exists(service, folder_id, file_name):
    """
    Check file is created or not. 

    Parameters:
        service: Объект сервиса Google Drive API.
        folder_id: Идентификатор папки Google Drive.
        file_name: Имя файла, который нужно найти.

    Returns:
        True, если файл найден, False - иначе.
    """
    # Gemini helps make query for Google API lib
    try:
        query = f"'{folder_id}' in parents and name = '{file_name}'"
        results = service.files().list(q=query, fields="files(id)").execute()
        items = results.get('files', [])

        return len(items) > 0

    except Exception as ex:
        logger.error(
            f'[{foo_name()}]'
            'Google API deny request. '
            f'Ex text: {str(ex)}. '
            f'Query: {query}'
        )

        return False

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
            or None if success or Google Drive API deny request
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
        service.files().create(body=file_metadata, media_body=media).execute()
        await remove_file(name)

        if await check_file_exists(
            service=service,
            folder_id=os.getenv("GOOGLE_DRIVE_DIRECTORY_ID"),
            file_name=name
        ):

            return True, None

        logger.error(
            f'[{foo_name()}]'
            'Exception while creating file. '
            'Create method works, but checking file method'
            'showed that there is no file. '
            f'Ex text: {str(ex)}. '
            F"Name: {name}. "
        )

        return False, None

    except Exception as ex:
        logger.error(
            f'[{foo_name()}]'
            f'Ex text: {str(ex)}'
        )

        return False, str(ex)
