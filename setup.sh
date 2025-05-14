# setup.sh
#!/bin/bash
echo "Building React frontend..."
cd frontend
yarn build
cd ..


# Collect static files (important for production, implementing now)
echo "Collecting static files..."
cd backend
python manage.py collectstatic --noinput
cd ..

# Move build files from React to the Django backend
echo "Moving build files to backend..."
cd frontend
cp -r build/* ../backend/

# Remove build files from the frontend
rm -r build/*
cd ..

# Remove duplicates in backend/staticfiles 
# created from "python manage.py collectstatic --noinput"
cd backend/staticfiles
rm -r "css" "js" *.json *.html *.ico
cd ..
python manage.py runserver