#FROM public.ecr.aws/debian/debian:bullseye
FROM debian:10
#FROM python:3 867MB big size
ENV APPDIR /var/www/html/app
RUN mkdir -p /var/www/html
COPY ../code $APPDIR
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y python3-pip
RUN apt install build-essential libssl-dev libffi-dev python3-dev python3-mysqldb default-libmysqlclient-dev -y
RUN apt install -y python3-venv
WORKDIR $APPDIR
RUN python3.7 -m venv _env
RUN . _env/bin/activate
RUN pip3 install -r requirements.txt 

CMD python3 manage.py runserver 0.0.0.0:80

EXPOSE 80/tcp