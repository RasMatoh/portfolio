#!/bin/bash
# Install dependencies
pip install -r requirements.txt --break-system-packages
 
# Collect static files
python manage.py collectstatic --noinput