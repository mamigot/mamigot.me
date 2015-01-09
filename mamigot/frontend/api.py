from flask import request, copy_current_request_context
import requests
import datetime


def caller(post_type, url_params):

    @copy_current_request_context
    def get_base_url():
        return 'http://' + request.host + "/api/"

    full_url = get_base_url() + post_type + "/posts" + url_params
    return requests.get(full_url)



def get_posts_list(post_type, limit):
    post_type = post_type.lower()
    if post_type not in ['blog', 'projects']:
        raise NotImplementedError('Given post_type is not implemented.')


    list_fields = ['title', 'slug', 'desc', 'created_at']

    fields_param = "fields=" + ",".join(list_fields)
    limit_param = "limit=" + str(limit) if limit else ""

    all_fields = [fields_param, limit_param]
    url_params = "?" + "&".join(all_fields)

    res = caller(post_type, url_params)
    return res
