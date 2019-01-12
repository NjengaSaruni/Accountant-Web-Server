FROM grahamdumpleton/mod-wsgi-docker:python-3.4-onbuild

COPY requirements/base.txt /code/requirements./base.txt
RUN python3 -m pip install -r requirements/base.txt

# Django managements to be ran after installation of dependencies
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80 443

#Specific settings for mod_wsgi-express server
CMD [ "--working-directory", ".", \
      "--url-alias", "/static", "/static", \
      "--application-type", "module", "config.wsgi" ]