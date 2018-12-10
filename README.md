# AccountantPlus Web Server

This repository contains the backend for the AccountantPlus web service. 

## How to run the server
1. ### Without docker (Linux | Ubuntu)

     
     $ git clone https://github.com/NjengaSaruni/Accountant-Web-Server.git
     $ cd Accountant-Web-Server
     
 If you do not have python and pip installed:
 
     $ sudo apt-get install python3 python3-pip virtualenvwrapper
     
 Use of a virtual environment is recommended and is good practice
     
     $ mkvirtualenv -p /usr/bin/python3 <venv_name>
     $ workon <venv_name>
 
 Install packages from the requirements folder.
     
     $ pip install -r requirements/base.txt
     
 This Web API uses a PostgreSQL database. You need a PostgreSQL server running locally.
     
     $ sudo apt-get install postgresql postgresql-contrib
     
 Add a database to your Postgres using. You may use `psql` as follows:
 
     $ sudo -su postgres psql postgres
 
 This will open an interactive terminal, where you can create a database, and a role
    
     > CREATE DATABASE <your_db_name>;
     > CREATE ROLE <your_user> LOGIN PASSWORD '<your_password>';
     > GRANT ALL PRIVILEGES ON DATABASE <your_db_name> TO <your_user>;
     > \q
 
 Copy the values of the `.sample_env` file into a new `.env` file
      
     $ cat .sample_env >> .env
     
 You can then use the `./manage.py` script to run migrations and run the dev server
 
     $ ./manage.py migrate
     $ ./manage.py createsuperuser
     $ ./manage.py runserver
     
 Maintained by [Peter](https://twitter.com/NjengaSaruni)