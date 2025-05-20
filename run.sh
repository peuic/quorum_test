#!/bin/bash

echo "Applying migrations..."
python manage.py migrate

echo "Importing Legislators..."
python manage.py import_csv Legislator data/legislators.csv

echo "Importing Bills..."
python manage.py import_csv Bill data/bills.csv

echo "Importing Votes..."
python manage.py import_csv Vote data/votes.csv

echo "Importing Vote Results..."
python manage.py import_csv VoteResult data/vote_results.csv

echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000