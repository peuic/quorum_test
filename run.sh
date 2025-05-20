#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Applying migrations..."
python manage.py migrate

echo "Loading initial data..."
python manage.py loaddata initial_data.json

echo "Loading Django Server..."
python manage.py runserver 0.0.0.0:8000