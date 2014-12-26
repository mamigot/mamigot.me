from flask import Flask
import config as config_vars # Custom config vars

# Blueprints
from api.api import api


# Create application
app = Flask(__name__)
# Saves config_vars into the app.config dict
app.config.from_object(config_vars)


# Blueprints
app.register_blueprint(api, url_prefix='/api')



'''
See all properties of the application
    print app.__dict__

    print app.url_map

    print app.blueprints['api'].__dict__

'''


if __name__ == '__main__':
    app.run()
