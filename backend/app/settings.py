import os

DEBUG = os.environ['LOG_LEVEL'].lower() == 'debug'

SECRET_KEY = os.environ['SECRET_KEY']

DB_URL = 'mysql+mysqldb://{user}:{password}@{host}/{database}?charset=utf8'.format(**{
    'user': 'root',
    'password': os.environ['MYSQL_ROOT_PASSWORD'],
    'host': 'db',
    'database': 'wouldlist'
})

ALLOW_ORIGINS = [
    "http://localhost:3000",
]
