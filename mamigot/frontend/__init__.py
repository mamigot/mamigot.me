from flask import Flask, make_response
import settings as config_vars # Custom config vars


app = Flask('mamigot.frontend')
app.config.from_object(config_vars)


#@app.route('/<path:path>')
@app.route('/')
def index(path=None):
    file = app.config['BASE_DIR'] + "/static/app/index.html"
    return make_response(open(file).read())
