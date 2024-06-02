FROM python:3.10.8 as Python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./Docker/Django_WSGI/requirements.txt /app
COPY ./app /app

RUN pip install -r requirements.txt

EXPOSE 8069

HEALTHCHECK CMD curl -sS http://localhost:8069 || exit 1

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8069"]

LABEL description="Image of Django application. Install packages and run Django project"