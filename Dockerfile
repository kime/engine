FROM python:3.6.8-slim-jessie

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 3785
CMD python3 -m engine