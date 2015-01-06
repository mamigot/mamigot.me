# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# http://flask-mongoengine.readthedocs.org/en/latest/
MONGODB_SETTINGS = {'DB': "mamigot_test"}


DEBUG = False
