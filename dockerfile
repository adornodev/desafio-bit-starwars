FROM python:3.7
ADD . /bit_api
WORKDIR /bit_api
RUN pip install -r requirements.txt