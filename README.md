# giphy-guessing-game

Download and install the latest stable version of Python from [https://www.python.org/downloads/](https://www.python.org/downloads/) for your operating system.

## Usage

1. Create a python virtual environment for the project. Type the following into your terminal

```sh
python3 -m venv virt
source virt/bin/activate
```

2. Install necessary python packages:

```sh
pip install django
pip install django-rest-framework
pip install django-cors-headers
pip install django-environ
```

3. Provide postgres database information in [backend/beckend/settings.py](backend/backend/settings.py)



```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "name_of_database",
        "USER": "postgres_username",
        "HOST": "localhost",
    	"PORT": "5432",
    }
}
```
