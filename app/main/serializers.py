""" Serializers for validating data that sent to web-server """
# Python imports
import os
import aiofiles
import asyncio

# DRF imports
from rest_framework import serializers

# import custom foos, classes and logger
from main.settings import logger

# import constants, config data
from main.constants import NOT_VALID_TYPE_ERROR

# etc
import magic  # python-magic


async def write_file(
        name,
        data
) -> tuple[bool, None | str]:
    """
    Create file with the sent request data.
    Parameters:
        drf_serializer_date: dict with field-value pair
            "name", "data" from the request data
    Returns:
        bool: success create or not
        None | str: None if success, str with exception
            if there is exception
    """
    try:
        mime_type = magic.from_file(name)

        if mime_type.startswith("text/"):

            async with aiofiles.open(name, 'w') as new_file:
                await new_file.write(data)

            return True, None

        else:

            raise serializers.ValidationError(
                code="pizda",
                detail=NOT_VALID_TYPE_ERROR
            )

    except Exception as ex:
        logger.error(str(ex))

        raise serializers.ValidationError(str(ex))


class CreateGoogleDocSerializer(serializers.Serializer):
    """
    Serializer class for validating POST request
    to create google doc
    """
    # allow_blank=False, trim_whitespace=True are defaul
    # https://www.django-rest-framework.org/api-guide/fields/#charfield
    data = serializers.CharField(allow_blank=True)
    name = serializers.CharField()

    def validate(self, attrs):
        """
        custom validation (built-in method)
        https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
        """
        drf_serializer_date = super().validate(attrs)

        try:
            asyncio.run(
                write_file(
                    name=drf_serializer_date["name"],
                    data=drf_serializer_date["data"]
                )
            )

            return drf_serializer_date["name"]

        except Exception as ex:

            raise ex