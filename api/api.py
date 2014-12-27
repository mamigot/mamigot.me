from flask import Blueprint

from ext import controller as ext_controller


api = Blueprint('api', __name__)


'''
Add support for a new external API by adding a rule here and mapping
it to a function in ext_controller.
'''
# The supported features from each external interface are
# defined in the functions within the controller.
api.add_url_rule('/linkedin/<string:item>',
                view_func = ext_controller.linkedin)

api.add_url_rule('/github/<string:item>',
                view_func = ext_controller.github)
