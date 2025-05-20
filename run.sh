#!/bin/bash

echo "Checking if dependencies are installed..."
pip install --upgrade pip
pip install -r requirements.txt || { echo "Failed to install dependencies. Exiting."; exit 1; }

echo "Applying migrations..."
python manage.py migrate || { echo "Failed to apply migrations. Exiting."; exit 1; }

echo "Importing Legislators..."
python manage.py import_csv Legislator data/legislators.csv || { echo "Failed to import Legislators. Exiting."; exit 1; }

echo "Importing Bills..."
python manage.py import_csv Bill data/bills.csv || { echo "Failed to import Bills. Exiting."; exit 1; }

echo "Importing Votes..."
python manage.py import_csv Vote data/votes.csv || { echo "Failed to import Votes. Exiting."; exit 1; }

echo "Importing Vote Results..."
python manage.py import_csv VoteResult data/vote_results.csv || { echo "Failed to import Vote Results. Exiting."; exit 1; }

echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000 || { echo "Failed to start Django server. Exiting."; exit 1; }