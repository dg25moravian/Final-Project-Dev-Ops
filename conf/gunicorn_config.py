command = '$(pwd)/.venv/bin/gunicorn'
pythonpath = '$(pwd)/django_website'
bind = '0.0.0.0:5555'
workers = 1
