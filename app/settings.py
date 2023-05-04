# myapp/settings.py
# SECRET_KEY = "your-secret-key-here"
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myapp",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "myappdb",
        "USER": "myappuser",
        "PASSWORD": "myapppassword",
        "HOST": "db",
        "PORT": 5432,
    }
}

STATIC_URL = "/static/"

TIME_ZONE = "JST"
