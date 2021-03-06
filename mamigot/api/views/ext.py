'''
Resources from external APIs
'''
from flask import Response, request, json, jsonify
from ..retrievers import rlinkedin, rgithub


supported = {
    "linkedin" : ["profile"],
    "github"   : ["repos"]
}


def linkedin(item):
    api_name = "linkedin"

    if item == "profile" and request.method == "GET":
        return ext_api_fetcher(api_name, item, rlinkedin.get_full_profile)

    else: return not_supported(api_name, item, request.method)


def github(item):
    api_name = "github"
    kwargs = {}

    # Limit the number of results
    limit = request.args.get('limit')
    if limit and limit > 0:
        kwargs["limit"] = int(limit)

    # Specify the order of returned repositories
    # See available sorting criteria here:
    # https://developer.github.com/v3/repos/
    sort = request.args.get('sort')
    if sort:
        kwargs["sort"] = sort

    if item == "repos" and request.method == "GET":
        return ext_api_fetcher(api_name, item, rgithub.get_repos, kwargs)

    else: return not_supported(api_name, item, request.method)


def ext_api_fetcher(api_name, wanted_item, fetcher_func, kwargs=None):

    if wanted_item in supported[api_name]:
        jsresp, status = fetcher_func(**kwargs) if kwargs else fetcher_func()

        if status == 200: # Add meta info
            pass

        else: # Add info about error from external service
            jsresp["external api name"] = api_name
            jsresp["status"] = status

        jsonstr = json.dumps(jsresp)
        return Response(jsonstr, status=status, mimetype='application/json')

    else: return not_supported(api_name, item, request.method)


def not_supported(ext_api_name, item, request_method):
    status = 501
    msg = "Error: item '%s' from %s's API is not supported." \
          % (item, ext_api_name)

    # jsonify() returns a Flask Response object
    # http://stackoverflow.com/questions/7907596/json-dumps-vs-flask-jsonify
    resp = jsonify({
            "requested from"  : ext_api_name,
            "requested item"  : item,
            "requested using" : request_method,
            "message"  : msg,
        })

    resp.status_code = status
    return resp
