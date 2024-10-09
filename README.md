# homework
Web-App for Homeworks and Assignments

Installation:
  - Make sure python 3.x installed
  - python3 -m pip install Django
  - python3 -m pip install psycopg2-binary
  - git clone the repo

Postgres Start:
  - start the postgresql using Dockerfile
      docker run --name my_postgres_container -p 5432:5432 -d custom-postgres
      docker exec -it my_postgres_container psql -U admin -d school

Application start:
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py runserver
