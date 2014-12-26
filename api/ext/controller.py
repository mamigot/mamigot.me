from flask import request

from retrievers import linkedin, github



'''
Interfaces to external APIs
'''

def linkedin(item):
    if item == "profile":
        if request.method red names== "GET":
            return "GET YOUR PROFILE!"

    else: # Unsupported
        return "unsupported"


def github(item):
    if item == "repos":
        return "THESE ARE YOUR REPOS!"

    else: # Unsupported
        return "unsupported"
