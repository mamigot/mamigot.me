

from api import api
from views import linkedin, github


api.add_url_rule('/linkedin/<string:item>',
                view_func = linkedin.linkedin)

api.add_url_rule('/github/<string:item>',
                view_func = github.github)
