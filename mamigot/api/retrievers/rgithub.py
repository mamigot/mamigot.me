from flask import json
import requests
import secret_credentials as secret


def get_repos(limit=None, sort=None):
    username = secret.sgithub['username']
    sort = sort if sort else "pushed"
    url = "https://api.github.com/users/" + username + "/repos?sort=" + sort

    r = requests.get(url)
    js = r.json()

    if r.status_code != 200:
        return { "error message" : js["message"] }, r.status_code


    trimmed = [] # Only take the following fields from GitHub's response
    wantedFields = [ 'name','full_name','html_url','description',
                     'created_at','updated_at','language' ]

    if limit: js = js[:limit]
    for repo in js:
        items = {w:repo[w] for w in wantedFields}
        trimmed.append( items )

    return { "content" : trimmed }, r.status_code
