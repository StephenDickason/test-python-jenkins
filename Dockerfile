FROM python:3.6-stretch

RUN pip install pytest

COPY ./python code/