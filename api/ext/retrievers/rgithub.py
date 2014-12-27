from flask import json
import requests

from secret import sgithub


def get_repos(limit=None):
    username = sgithub['username']
    url = "https://api.github.com/users/" + username + "/repos?sort=updated"

    r = requests.get(url)
    if r.status_code != 200:
        return r.text, r.status_code

    js = r.json()
    if limit: js = js[:limit]

    # Trim output (don't need all of it)
    trimmed = []
    wantedFields = [ 'name','full_name','html_url','description',
                     'created_at','updated_at','language' ]

    for repo in js:
        items = {w:repo[w] for w in wantedFields}
        trimmed.append( items )


    return json.dumps(trimmed), r.status_code
