FROM python:slim

WORKDIR /Final-Project-Dev-Ops

COPY requirements.txt .

RUN python3 -m venv .venv
RUN .venv/bin/pip3 install -r requirements.txt

WORKDIR /django_website

COPY website.env .env

CMD ["manage.py", "runserver"]

CMD [".venv/bin/gunicorn", "--bind", "0.0.0.0:80", "app:app"]
