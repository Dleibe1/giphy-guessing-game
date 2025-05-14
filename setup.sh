#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status.

echo "Building React frontend..."
cd frontend
yarn build # This creates the frontend/build directory
cd .. # Back to project root (giphy-guessing-game/)

echo "Preparing Django project directories for React build..."
# Ensure target directories exist
mkdir -p backend/templates  # For index.html
mkdir -p backend/static     # For React's static assets (JS, CSS, media, favicon, manifest etc.)

echo "Cleaning old React build artifacts from Django project..."
rm -f backend/templates/index.html
# Clear out backend/static/ to ensure no stale React files from previous builds.
# This deletes the *contents* of backend/static/, not the directory itself.
find backend/static -mindepth 1 -delete

echo "Copying React build files to Django project..."
# 1. Copy React's index.html to Django's templates directory
#    (Ensure backend/backend/settings.py TEMPLATES DIRS includes BASE_DIR / "templates")
cp frontend/build/index.html backend/templates/

# 2. Copy contents of React's build/static/ directory (CSS, JS, media)
#    into Django's project-level static directory (backend/static/).
#    (Ensure backend/backend/settings.py STATICFILES_DIRS includes BASE_DIR / "static")
cp -r frontend/build/static/* backend/static/

# 3. Copy other root assets from React's build directory (favicon, manifest, etc.)
#    into Django's project-level static directory (backend/static/).
#    These will then be picked up by collectstatic.
#    Using '2>/dev/null || true' to prevent script failure if a file doesn't exist.
cp frontend/build/*.ico backend/static/ 2>/dev/null || true
cp frontend/build/manifest.json backend/static/ 2>/dev/null || true
cp frontend/build/asset-manifest.json backend/static/ 2>/dev/null || true
cp frontend/build/robots.txt backend/static/ 2>/dev/null || true
# If you have logo images like logo192.png, logo512.png at the root of frontend/build:
cp frontend/build/logo*.png backend/static/ 2>/dev/null || true
# Add any other specific file types or names if necessary (e.g., .webmanifest, .xml)

# Optional: Clean up React's build directory now that files are copied
# echo "Removing React build directory..."
rm -rf frontend/build

echo "Collecting all Django static files..."
cd backend
# collectstatic will gather files from:
# - backend/static/ (where we just put React assets)
# - Django admin's static files
# - Any other app's static/ directories (e.g., api_app/static/)
# And place them into STATIC_ROOT (backend/staticfiles/)
# Using --clear ensures STATIC_ROOT is emptied before collecting new files.
python manage.py collectstatic --noinput --clear
cd .. # Back to project root

echo "Starting Django server..."
cd backend
python manage.py runserver