FROM python:3.9-slim-buster

LABEL maintainer "Timo Ufermann, timo@tiu-webapplications.de"

# set working directory in container
WORKDIR /usr/app

# Copy and install packages
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r /requirements.txt

# Copy app folder to app folder in container
COPY . /usr/app

# Changing to non-root user
RUN useradd -m exec-user
RUN chown exec-user temp
USER exec-user

# Run locally on port defined in .env file
CMD gunicorn --bind 0.0.0.0:${EXT_PORT} app:server