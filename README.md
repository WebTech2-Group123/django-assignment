# Assignment 7 - Django

[![Build Status](https://travis-ci.org/WebTech2-Group123/django-assignment.svg?branch=master)](https://travis-ci.org/WebTech2-Group123/django-assignment)
[![Coverage Status](https://coveralls.io/repos/WebTech2-Group123/django-assignment/badge.svg?branch=master&service=github)](https://coveralls.io/github/WebTech2-Group123/django-assignment?branch=master)

## Notes
We send a link at the user registration to verify the email address. In order to do this, the app need a SMTP server (we used [SendGrid](https://sendgrid.com/) locally). There are 2 possibilities to test the email functionality:
 * Use the Django Console backend
 * Configure a SMTP server

### Use the Django Console backend (default)
The project uses by default django.core.mail.backends.console.EmailBackend. The emails will be print in the console stdout instead of sent over SMTP. See https://docs.djangoproject.com/en/1.9/topics/email/#console-backend for details.

### Configure a SMTP server
Set the following environment variables before running the project:
```bash
export EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
export EMAIL_HOST="SMTP host"
export EMAIL_HOST_USER="SMPT user"
export EMAIL_HOST_PASSWORD="SMPT user"
export EMAIL_PORT="SMPT port"             # if not 587
export EMAIL_USE_TLS="SMPT use TSL"       # if not True
```

## Deploy the project
Clone this repository
```bash
git clone https://github.com/WebTech2-Group123/django-assignment.git
cd django-assignment
```
Create a virtual environment for Python 3.4
```bash
virtualenv --no-site-packages -p /usr/bin/python3.4 env
source env/bin/activate
```
Install dependencies
```bash
pip install -r requirements.txt 
```
Run the project
```bash
cd blog
python manage.py migrate
python manage.py createsuperuser    # optional, only if you need it
python manage.py runserver
```
Open a browser at http://localhost:8000/


## Tasks
 * [x] Blog:
    * [x] see posts
    * [x] add post
    * [x] login
 * [x] Third Party Package
 * [x] Test model unit
 * [x] Functional Test (optional)
    * [x] login
    * [x] add post
    * [x] check new post's list
