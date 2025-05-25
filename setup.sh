#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status.

echo "Building React frontend..."
cd frontend
yarn build 
cd .. 

echo "Collecting all Django static files..."
cd backend
python manage.py collectstatic --noinput --clear
cd ..

echo "Starting Django server..."
cd backend
python manage.py runserver