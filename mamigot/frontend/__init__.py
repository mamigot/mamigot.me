from flask import Flask
import settings as config_vars # Custom config vars


app = Flask('mamigot.frontend')
app.config.from_object(config_vars)


import urls # After app is created, add url_rules


# Configure assets
from assets import init_app
init_app(app)
