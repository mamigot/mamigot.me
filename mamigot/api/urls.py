from mamigot.api import app
from views import linkedin, github


app.add_url_rule('/linkedin/<string:item>',
                view_func = linkedin)

app.add_url_rule('/github/<string:item>',
                view_func = github)
