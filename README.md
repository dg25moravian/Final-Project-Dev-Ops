# Final-Project-Dev-Ops

This project is a Django website that uses redis allow connections from anywhere

# Contributors

Davin Glynn - dg25moravian

Jeffery Eisenhardt - eisenhardtj

Dermot Badman - Dbad0210

# Steps before you run locally

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# How to run locally

After you do those steps, you will then run 

```
python manage.py runserver
```

# How to run with Gunicorn

```
gunicorn -c conf/gunicorn_config.py personal_portfolio.wsgi
```
