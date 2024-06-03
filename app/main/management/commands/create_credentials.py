# Python imports
from os import getenv, getcwd
import json

# Django import
from django.core.management.base import BaseCommand

# import JSON credential blank
from main.management.commands.json_blank import CREDENTIALS_JSON


class Command(BaseCommand):
    help = "Create credentials JSON"

    def handle(self, *args, **options):
        dict_json = CREDENTIALS_JSON.copy()

        # get all json params from env
        dict_json["project_id"] = getenv("PROJECT_ID")
        dict_json["private_key"] = getenv("PRIVATE_KEY")
        dict_json["private_key_id"] = getenv("PRIVATE_KEY_ID")
        dict_json["client_email"] = getenv("CLIENT_EMAIL")
        dict_json["client_id"] = getenv("CLIENT_ID")

        # https://stackoverflow.com/a/65478209
        credentials_json = json.dumps(dict_json).replace('\\\\', "\\")

        with open('credentials.json', 'w') as f:
            f.write(credentials_json)

        self.stdout.write('Credentials json created!')

