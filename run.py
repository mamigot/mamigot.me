from flask import Flask
import config as config_vars # Custom config vars


# Create application
app = Flask(__name__)
# Saves config_vars into the app.config dict
app.config.from_object(config_vars)



if __name__ == '__main__':
    app.run()
