from flask import request

'''
Interfaces to external APIs
'''

def linkedin(item):
    if item == "profile":
        if request.method == "GET":
            return "GET YOUR PROFILE!"

    else: # Unsupported
        return "unsupported"


def github(item):
    if item == "repos":
        return "THESE ARE YOUR REPOS!"

    else: # Unsupported
        return "unsupported"
