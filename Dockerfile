FROM python:3.10.8-alpine3.16

WORKDIR /application
COPY requirements.txt ./requirements.txt
RUN pip3 install -r ./requirements.txt
COPY app ./app
EXPOSE 8000

CMD unicorn main:app --reload