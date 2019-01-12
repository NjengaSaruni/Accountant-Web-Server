FROM grahamdumpleton/mod-wsgi-docker:python-3.4-onbuild

COPY requirements/base.txt /code/requirements./base.txt
RUN python3 -m pip install -r requirements/base.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80 3500

CMD [ "--working-directory", ".", \
      "--url-alias", "/static", "/static", \
      "--application-type", "module", "config.wsgi" ]

