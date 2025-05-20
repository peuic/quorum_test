FROM python:3.7-slim


WORKDIR /app


COPY . /app


RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8000

CMD ["sh", "-c", "echo 'Access application through: http://localhost:8000' && python manage.py migrate && python manage.py import_csv Legislator data/legislators.csv && python manage.py import_csv Bill data/bills.csv && python manage.py import_csv Vote data/votes.csv && python manage.py import_csv VoteResult data/vote_results.csv && python manage.py runserver 0.0.0.0:8000"]