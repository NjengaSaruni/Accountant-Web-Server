FROM ubuntu

RUN apt-get update && apt-get install -y apt-utils vim curl apache2 apache2-utils

RUN apt-get -y install python3 libapache2-mod-wsgi-py3
RUN ln /usr/bin/python3 /usr/bin/python

RUN apt-get -y install python3-pip
RUN ln /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip

ADD ./apache.conf /etc/apache2/sites-available/000-default.conf

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

COPY requirements/base.txt /code/requirements./base.txt

WORKDIR /code
COPY . /code/

RUN python3 -m pip install -r requirements/base.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80 3500
CMD ["apache2ctl", "-D", "FOREGROUND"]