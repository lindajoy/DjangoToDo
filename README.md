# EasySolar
A simple project with django (backend ) and flutter (frontend)

Built a Django Application , added Django REST framework Application and <b>django_rest_auth</b> to handle authentication.

## Django - SRC Folder
Core is written in Python3.7 and Django 2.2

## Setup

* First, clone the repository:

```sh
git clone https://github.com/lindajoy/EasySolar
cd src
```

* Create a virtual environment to install dependencies in and activate it:


```sh
pipenv --python 3.7 install django==2.2
pipenv shell
```


* Run database migrations with this command

```sh
python3 manage.py migrate
```

* Run server to ensure everything is working properly.

```sh
python3 manage.py runserver
```
My Endpoints include:
```
http://127.0.0.1:8000/api/v1/  - Shows the lists of things to be done
http://127.0.0.1:8000/api/v1/1/ - Shows the details of a specific list
http://127.0.0.1:8000/api/v1/rest-auth/login/ - Django Authentication
http://127.0.0.1:8000/api/v1/rest-auth/logout/ - For users to logout
```
# Frontend

## open new terminal and go to the flutter_app
cd flutter_app
## get flutter packages
flutter packages get
## run Flutter project
flutter run
```
