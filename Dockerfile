FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    python3.7 \
    python3-pip

WORKDIR /

COPY . /app

RUN pip3 install --upgrade pip 

RUN pip3  install -r /app/requirements.txt 

ENV FLASK_APP=app
ENV  LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

EXPOSE 5000 

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]