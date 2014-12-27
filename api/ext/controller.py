from flask import Response, json, jsonify
from retrievers import rlinkedin, rgithub

'''
Interfaces to external APIs
'''

def linkedin(item):
    if item == "profile":
        content, status = rlinkedin.get_full_profile()

        if status != 200: # Error message from LinkedIn
            msg = json.loads(content)["message"]
            content = ext_api_error("linkedin", msg, status)

        return Response(content, status=status, mimetype='application/json')

    else: return not_implemented("linkedin")


def github(item):
    if item == "repos":
        content, status = rgithub.get_repos(limit=None)

        if status != 200: # Error message from GitHub
            msg = json.loads(content)["message"]
            content = ext_api_error("github", msg, status)

        return Response(content, status=status, mimetype='application/json')

    else: return not_implemented("github")


def not_implemented(ext_api_name):
    status = 501

    # jsonify() returns a Flask Response object
    # http://stackoverflow.com/questions/7907596/json-dumps-vs-flask-jsonify
    resp = jsonify({
            "api"    : ext_api_name,
            "status" : status,
            "error"  : "This feature is not implemented.",
        })

    resp.status_code = status
    return resp


def ext_api_error(ext_api_name, ext_error_message, status):
    # Conveys errors from external APIs
    return json.dumps({
                "external api name"  : ext_api_name,
                "external error msg" : ext_error_message,
                "status" : status,
            })
