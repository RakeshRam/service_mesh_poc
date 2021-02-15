# Pull Official Base Image
FROM python:3.7-alpine

# Set Environment varibles
# Prevents Python from writing pyc files to disc 
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /src/main

# Update For MySQL for python-alpine
RUN apk update
RUN apk add musl-dev mariadb-dev gcc

# Install Dependencies
COPY requirements.txt /src/main/requirements.txt
RUN pip install -r requirements.txt

# Copy Project
COPY . /src/main