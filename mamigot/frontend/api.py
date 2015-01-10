from flask import request, copy_current_request_context
import requests
import datetime


def format_date(date_str, input_format='%Y-%m-%d %H:%M:%S.%f'):
    if not date_str: return ""

    dt_obj = datetime.datetime.strptime(date_str, input_format)

    output_format = '%b %d %Y'
    return dt_obj.strftime(output_format)


def issue_get_request(post_type, url_params):

    @copy_current_request_context
    def get_base_url():
        return 'http://' + request.host + "/api/"

    full_url = get_base_url() + post_type + "/posts" + url_params
    return requests.get(full_url)


def get_posts_list(post_type, limit="", addl_url_params=None):
    '''
    addl_url_params is a dictionary
    '''
    post_type = post_type.lower()
    if post_type not in ['blog', 'projects']:
        raise NotImplementedError('Given post_type is not implemented.')

    # All we need for a list representation
    relevant_fields = ['title', 'slug', 'desc', 'created_at']

    # The following parameters will be used to call the REST API
    url_params = {
                    "fields" : ",".join(relevant_fields),
                    "limit"  : str(limit) if limit else ""
                 }

    # Combine existing parameters with those provided by the user
    if addl_url_params and type(addl_url_params) is dict:
        url_params = dict( url_params.items() + addl_url_params.items() )

    stringified_params = [ (k + "=" + v) for k,v in url_params.iteritems() ]
    url_vars = "?" + "&".join(stringified_params)

    content = issue_get_request(post_type, url_vars).json()
    # Format dates
    for post in content:
        post["created_at"] = format_date( post["created_at"] )

    return content[::-1] # Show most recent first
