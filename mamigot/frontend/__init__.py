from flask import Flask
import settings as config_vars # Custom config vars


app = Flask('frontend')
app.config.from_object(config_vars)
