from flask import Response, json, jsonify

from retrievers import rlinkedin, rgithub

'''
Interfaces to external APIs
'''

def linkedin(item):
    if item == "profile":
        content, status = rlinkedin.get_full_profile()

        if status != 200:
            js = json.loads(content) # Access error message from LinkedIn
            msg = js["message"]
            content = json.dumps({
                        "api" : "linkedin",
                        "error" : msg,
                        "status" : status,
                    })

        return Response(content, status=status, mimetype='application/json')

    else: return not_implemented("linkedin")


def github(item):
    if item == "repos":
        return "THESE ARE YOUR REPOS!"

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
