FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN apt-get update

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
# add gettext for makemessages command
RUN apt-get update && apt-get install -y gettext