# setup.sh
#!/bin/bash
echo "Building React frontend..."
cd frontend
yarn build:django
cd ..

echo "Collecting static files..."
cd backend
python manage.py collectstatic --noinput
python manage.py runserver