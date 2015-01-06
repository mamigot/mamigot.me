from flask.ext.assets import Environment, Bundle


css_app = Bundle("css/main.css", # Add other custom CSS files here
                 filters="cssmin", output="css/mamigot.css")

'''
Add other CSS and JS assets here and register them below
'''


def init_app(app):
    assets = Environment(app)
    assets.register('css_app', css_app)

    assets.cache = not app.debug
