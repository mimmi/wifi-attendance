import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    INTEGRATION_KEY = os.environ.get('INTEGRATION_KEY') or 'INSERT_INTEGRATION_KEY_HERE'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'INSERT_RANDOM_KEY_HERE'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False