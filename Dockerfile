FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN set -e;

ADD . /app/
WORKDIR /app/

RUN apk add --no-cache postgresql-client
RUN apk add --no-cache --virtual .build-deps \
        gcc \
        linux-headers \
        postgresql-dev \
        musl-dev \
        python3-dev && \
        pip3.6 install -r requirements/app.txt --no-cache-dir && \
        apk del .build-deps

CMD ["uwsgi", "--ini", "system_templates/uwsgi.ini"]