#!/bin/bash
# Runs during Vercel build to collect all static files into /staticfiles
python manage.py collectstatic --noinput