FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3.8

COPY ./env/requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD ["deploy/app.py"]
