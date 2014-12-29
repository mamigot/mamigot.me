from flask import Response, json, jsonify
from retrievers import rlinkedin, rgithub

'''
Interfaces to external APIs
            ###CHANGE TO CLASS-BASED VIEWS WITH ONLY A GET() OPTION
'''

implemented = {
    "linkedin" : ["profile"],
    "github"   : ["repos"]
}

def linkedin(item):
    api_name = "linkedin"

    if item == "profile":
        return ext_api_fetcher(api_name, item, rlinkedin.get_full_profile)

    else: return not_implemented(api_name)


def github(item):
    api_name = "github"

    if item == "repos":
        return ext_api_fetcher(api_name, item, rgithub.get_repos)

    else: return not_implemented(api_name)


def ext_api_fetcher(api_name, wanted_item, fetcher_func):

    if wanted_item in implemented[api_name]:
        jsresp, status = fetcher_func() #jsresp is a dict

        if status == 200: # Add meta info
            pass

        else: # Add info about error from external service
            jsresp["external api name"] = api_name
            jsresp["status"] = status

        jsonstr = json.dumps(jsresp)
        return Response(jsonstr, status=status, mimetype='application/json')

    else: return not_implemented(api_name)


def not_implemented(ext_api_name):
    status = 501

    # jsonify() returns a Flask Response object
    # http://stackoverflow.com/questions/7907596/json-dumps-vs-flask-jsonify
    resp = jsonify({
            "api"    : ext_api_name,
            "status" : status,
            "error"  : "I have not implemented this feature.",
        })

    resp.status_code = status
    return resp
