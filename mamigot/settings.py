'''
Configuration variables for the main app
'''
# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# http://flask-mongoengine.readthedocs.org/en/latest/
MONGODB_SETTINGS = {'DB': "mamigot_test"}


# True only for development environment
DEBUG=True


# TBD
SECRET_KEY='tobedetermined'
