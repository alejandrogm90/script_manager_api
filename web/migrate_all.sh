#!/bin/bash

pipenv run python manage.py makemigrations script_manager
pipenv run python manage.py migrate script_manager
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
