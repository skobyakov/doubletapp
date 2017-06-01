DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

MONGODB_SETTINGS = {
    'db' : 'test',
    'host' : '127.0.0.1',
    'port' : 27017
}

DOMAIN = {
    'Advertising Companies' : {

    }
}

CSRF_ENABLED = True


CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"