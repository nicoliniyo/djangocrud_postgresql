#!/bin/bash
#python manage.py runserver

python -m gunicorn djangocrud.asgi:application -k uvicorn.workers.UvicornWorker
