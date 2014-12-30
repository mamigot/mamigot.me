# Creates Flask application object for the API
# Imports views and urls (import api.views)

from flask import Flask
app = Flask(__name__)

import urls
