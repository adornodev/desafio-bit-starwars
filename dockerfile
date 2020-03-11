FROM python:3.7

ADD . /bit_api
WORKDIR /bit_api

ENV FLASK_ENV "development"
ENV FLASK_APP "app"

RUN pip install -r requirements.txt

EXPOSE 5000

CMD flask run --host=0.0.0.0