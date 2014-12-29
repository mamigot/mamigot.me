# Global Flask application object (configured) and the database

from flask import Flask
import config as config_vars # Custom config vars


# Create application
app = Flask(__name__)
app.config.from_object(config_vars)


# Launch database
# db = ...
