from flask import Flask
import settings as config_vars # Custom config vars


app = Flask('mamigot.api')
app.config.from_object(config_vars)


# Launch database
from flask.ext.mongoengine import MongoEngine
db = MongoEngine(app)


import urls # After app is created, add url_rules
