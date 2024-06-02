# Python imports
import asyncio
import time
import logging

# DRF imports
# https://www.django-rest-framework.org/api-guide/views/#view-schema-decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# import serializers
from main.serializers import CreateGoogleDocSerializer

# import custom foos, classes
from main.serivces import google_drive_post_request
from main.utils import foo_name

# import logger
from main.settings import logger


@api_view(['POST'])
def create_google_doc(request) -> Response:
    """
    Post request handler, run creating file and
    send file to Google Drive API.
    """
    start_time = time.time()

    serializer = CreateGoogleDocSerializer(data=request.data)

    if serializer.is_valid():

        if asyncio.run(
            google_drive_post_request(serializer.validated_data)
        ):

            return Response(
                status=HTTP_200_OK,
                data={
                    "time": f"{(time.time() - start_time):.6f}"
                }
            )
    
    else:
        return Response(
            status=HTTP_400_BAD_REQUEST,
            data=serializer.error_messages
        )


