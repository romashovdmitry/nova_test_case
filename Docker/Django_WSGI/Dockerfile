FROM python:3.10.8 as Python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8069

WORKDIR /app

COPY ./Docker/Django_WSGI/requirements.txt /app
COPY ./Docker/Django_WSGI/entrypoint.sh /app
COPY ./app /app
COPY ./static /app/static

RUN pip install --no-cache-dir -r requirements.txt

HEALTHCHECK CMD curl -sS http://localhost:8069/api/docs/ || exit 1

RUN chmod +x /app/entrypoint.sh
# for Windows users, just in case, auto-changing
# format line ending of entrypoint.sh to Linux format.
# GPT helps with next 2 strings. 
RUN apt-get update && apt-get install -y dos2unix
RUN dos2unix /app/entrypoint.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh"]

LABEL description="Image of Django application. Install packages and run Django project"
