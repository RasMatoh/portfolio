#!/bin/bash
# Install dependencies first
pip install -r requirements.txt
 
# Collect static files
python manage.py collectstatic --noinput