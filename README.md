# giphy-guessing-game

Download and install the latest stable version of Python from [https://www.python.org/downloads/](https://www.python.org/downloads/) for your operating system.

## Usage

1. Create a python virtual environment for the Django project. Type the following into your terminal:

```sh
python3 -m venv virt
source virt/bin/activate
```

2. Install necessary python packages:

```sh
# From the root directory:
cd backend
pip install -r requirements.txt
```

3. Configure Environment Variables:

Create a `.env` file in the `backend` directory based on the example template:

```sh
# From the root directory
cp backend/.env.example backend/.env
```

Then edit `backend/.env` to configure your application:

```sh
# Database Configuration
DB_NAME=your_db_name          # Name of your PostgreSQL database
DB_USER=your_db_username      # PostgreSQL username
DB_PASSWORD=your_db_password  # PostgreSQL password (if needed)
DB_HOST=localhost             # Database host address
DB_PORT=5432                  # PostgreSQL port

# Security
SECRET_KEY=your_secret_key_here  # Generate using: python -c "import secrets; print(secrets.token_urlsafe(50))"

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000  # URLs allowed to access API

# Application Settings
DEBUG=True  # Set to False in production
```

4. Make database migrations and run the migrations:

```sh
python3 manage.py makemigrations
python3 manage.py migrate
```
5. Create a superuser for the Django project:

```sh
python3 manage.py createsuperuser
```

6. Make the setup.sh file executable:

```sh
chmod +x setup.sh
```

7. Run the setup.sh file to build and serve the React app:

```sh
# From the root directory (the directory containing setup.sh):
./setup.sh
```

8. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/).