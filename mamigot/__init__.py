# Global Flask application object (configured) and the database

from flask import Flask
import settings as config_vars # Custom config vars


# Create main application
app = Flask(__name__)
app.config.from_object(config_vars)


# Launch database
# db = ...
