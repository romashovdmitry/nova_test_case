# nova_test_case

Test case for Nova with Google Drive API.

## Quick Start

1. Clone the repository

```
git init
git clone https://github.com/romashovdmitry/nova_test_case
```

2. There is a files:

- example.env.
- credentiall_example.json

open those files, pass your comfortable values to variables and change name to 

- .env
- credentials.json

5. Run docker-compose 

```
docker compose up --build
```

# Swagger UI

Link to [Swagger UI](http://81.31.244.30:9000/api/docs/)

# API:
POST: http://81.31.244.30:9000/api/v1/google_drive_api/create_google_doc/

JSON: 
```
{"name": "string", "data": "string"}
```

# TODO:

- validation of not text files formats: now you can save file with text, but e.g. png, mp3, etc formats
- more tests
- SSL server

# NOTE:

### There is a size limit for uploading files on server equal to 5.12 MB. 
