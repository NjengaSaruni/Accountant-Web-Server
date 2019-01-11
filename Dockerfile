FROM python:3.6-alpine

RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
ADD ./nginx.conf /etc/apache2/sites-available/000-default.conf


ENV PYTHONUNBUFFERED 1
RUN mkdir /code

COPY base/requirements.txt /code/requirements./base.txt

WORKDIR /code
COPY . /code/


RUN update-ca-certificates

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements/base.txt --no-cache-dir && \
 apk --purge del .build-deps


COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

FROM ubuntu
RUN apt-get update
RUN apt-get -y install python-pip apache2 libapache2-mod-wsgi
RUN pip install — upgrade pip
RUN pip install djangorestframework
ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ADD ./nginx.conf /etc/apache2/sites-available/000-default.conf
ADD ./www/ /var/www/html
RUN chmod 664 /var/www/html/tutorial/tutorial/db.sqlite3
RUN chmod 775 /var/www/html/tutorial/tutorial
RUN chown :www-data /var/www/html/tutorial/tutorial/db.sqlite3
RUN chown :www-data /var/www/html/tutorial/tutorial
EXPOSE 80 3500
CMD [“apache2ctl”, “-D”, “FOREGROUND”]