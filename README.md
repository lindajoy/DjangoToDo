# EasySolar
A simple project with django (backend ) and flutter (frontend)

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