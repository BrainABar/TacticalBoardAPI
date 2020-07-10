# pull offical image
FROM python:3.8.1-alpine

# set work directory
WORKDIR /usr/src/app

# set enviroment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONBUFFERED 1

# copy requirements file
COPY ./requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN set -eux \
    && apk update \
    && apk add --no-cache postgresql-dev \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && python -m pip install --upgrade pip setuptools wheel \
    && python -m pip install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . /usr/src/app/

EXPOSE 8080

# CMD ['uvicorn', 'run:app', '--host', '0.0.0.0', '--port', '8080']