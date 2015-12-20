# Assignment 7 - Django

[![Build Status](https://travis-ci.org/WebTech2-Group123/django-assignment.svg?branch=master)](https://travis-ci.org/WebTech2-Group123/django-assignment)
[![Coverage Status](https://coveralls.io/repos/WebTech2-Group123/django-assignment/badge.svg?branch=master&service=github)](https://coveralls.io/github/WebTech2-Group123/django-assignment?branch=master)

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
