import os

DEBUG = os.getenv("DEBUG") == "True"
SECRET_KEY = os.getenv("SECRET_KEY")