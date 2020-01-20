import os

DEBUG = os.environ['LOG_LEVEL'].lower() == 'debug'

SECRET_KEY = os.environ['SECRET_KEY']

DB_CONFIG = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': 'db',
                'port': '3306',
                'user': 'root',
                'password': os.environ['MYSQL_ROOT_PASSWORD'],
                'database': 'wouldlist',
            }
        },
    },
    'apps': {
        'models': {
            'models': ['app.models'],
            'default_connection': 'default',
        }
    }
}

ALLOW_ORIGINS = [
    "http://localhost:3000",
]
