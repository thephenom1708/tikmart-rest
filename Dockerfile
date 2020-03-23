# pull official base image
FROM python:3.8.1

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY app/requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY app/. /usr/src/app/

# ENTRYPOINT ["/usr/src/app/", "manage.py"]
# CMD ["runserver", "0.0.0.0:9000"]