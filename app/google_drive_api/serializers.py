""" Serializers for validating data that sent to web-server """
# Python imports
import os
import aiofiles
import asyncio

# DRF imports
from rest_framework import serializers

# import constants
from google_drive_api.constants import (
    NOT_VALID_TYPE_ERROR,
    TOO_LARGE_FILE,
    FILE_SIZE_LIMIT
)

# import custom foos, classes and logger
from main.settings import logger
from main.utils import foo_name


async def write_file(
        name: str,
        data: str
) -> tuple[bool, None | str]:
    """
    Create file with the sent request data.

    Parameters:
        name: string value for param name file
            from user's request JSON
        data: string value for param name data 
            from user's request JSON
    
    Returns:
        bool: success create or not
        None | str: None if success, string with
            exception if there is exception
    """
    try:
        async with aiofiles.open(name, 'w') as new_file:

            await new_file.write(data)
            # https://developers.google.com/drive/api/reference/rest/v3/files/create
            # there is a size limit equal to 5,120 GB
            # fot tests on local setup to 5,12 MB
            # look at TOO_LARGE_FILE
            file_size = await new_file.tell()  
        
            if not file_size <= FILE_SIZE_LIMIT:

                return False, TOO_LARGE_FILE

            return True, None

    except Exception as ex:
        logger.error(
            f'[{foo_name()}] '
            f'Ex text: {str(ex)}'
        )
        return False, NOT_VALID_TYPE_ERROR


class CreateGoogleDocSerializer(serializers.Serializer):
    """
    Serializer class for validating POST request
    to create google doc
    """
    # allow_blank=False, trim_whitespace=True are default
    # https://www.django-rest-framework.org/api-guide/fields/#charfield
    data = serializers.CharField(allow_blank=True)
    name = serializers.CharField()

    def validate(self, attrs):
        """
        custom validation (built-in method)
        https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
        """
        drf_serializer_date = super().validate(attrs)

        bool_, exc = asyncio.run(
            write_file(
                name=drf_serializer_date["name"],
                data=drf_serializer_date["data"]
            )
        )

        if not bool_:
            raise serializers.ValidationError(exc)

        return drf_serializer_date["name"]
