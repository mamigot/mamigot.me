# Global Flask application object (configured) and the database
from flask import Flask
from flask.ext.mongoengine import MongoEngine
import settings as config_vars # Custom config vars


app = Flask('main')
app.config.from_object(config_vars)


# Launch database
db = MongoEngine(app)
