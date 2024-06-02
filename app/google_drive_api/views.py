# Python imports
import asyncio
import time

# DRF imports
# https://www.django-rest-framework.org/api-guide/views/#view-schema-decorator
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.serializers import ValidationError

# import serializers
from google_drive_api.serializers import CreateGoogleDocSerializer

# import constants
from google_drive_api.constants import GOOGLE_DRIVE_API_DENY_REQUEST

# import custom foos, classes
from google_drive_api.serivces import google_drive_post_request
from main.utils import foo_name

# import logger
from main.settings import logger


@api_view(['POST'])
@parser_classes([JSONParser])
def create_google_doc(request) -> Response:
    """
    Post request handler, run creating file and
    send file to Google Drive API.
    """
    start_time = time.time()
    try:
        serializer = CreateGoogleDocSerializer(data=request.data)
        if serializer.is_valid():

            if asyncio.run(
                google_drive_post_request(serializer.validated_data)
            )[0]:

                return Response(
                    status=HTTP_200_OK,
                    data={
                        "time": f"{(time.time() - start_time):.6f}"
                    }
                )

            else:
                return Response(
                    status=HTTP_400_BAD_REQUEST,
                    data={
                        **GOOGLE_DRIVE_API_DENY_REQUEST
                    }
                )

        else:
            return Response(
                status=HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    except Exception as ex:
        f'[{foo_name()}]'
        f'Ex text: {str(ex)}'
        return Response(
            str(ex),
            status=HTTP_400_BAD_REQUEST
        )
