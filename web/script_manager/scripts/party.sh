#!/bin/bash

cd "$HOME/Proyectos/coomer_party" || exit 1
pipenv run python main.py "$@"
