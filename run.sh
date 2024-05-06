#!/bin/bash
#python manage.py runserver

python -m gunicorn tasks.asgi:application -k uvicorn.workers.UvicornWorker
