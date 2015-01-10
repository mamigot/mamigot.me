from flask import request, copy_current_request_context
import requests
import datetime


def format_date(date_str, input_format='%Y-%m-%d %H:%M:%S.%f'):
    if not date_str: return ""

    dt_obj = datetime.datetime.strptime(date_str, input_format)

    output_format = '%b %d %Y'
    return dt_obj.strftime(output_format)


def issue_get_request(relative_url):

    @copy_current_request_context
    def get_base_url():
        return 'http://' + request.host

    full_url = get_base_url() + relative_url
    return requests.get(full_url)


def get_posts_list(post_type, limit="", addl_url_params=None):
    '''
    addl_url_params is a dictionary
    '''
    post_type = post_type.lower()
    if post_type != 'blog' and post_type != 'projects':
        raise NotImplementedError

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
    relative_url = "/api/" + post_type + "/posts" + url_vars

    r = issue_get_request(relative_url)
    js_content = r.json()

    # Format date (we know that the only fetched date is "created_at")
    for post in js_content:
        post["created_at"] = format_date( post["created_at"] )

    return js_content[::-1] # Show most recent first


def get_single_post(post_type, slug):
    post_type = post_type.lower()
    if post_type != 'blog' and post_type != 'projects':
        raise NotImplementedError

    relative_url = "/api/" + post_type + "/posts/" + slug

    r = issue_get_request(relative_url)
    if r.status_code is not 200:
        raise r.raise_for_status()

    js_content = r.json()

    # Format dates
    for post in js_content:
        post["created_at"] = format_date( post["created_at"] )
        post["modified_at"] = format_date( post["modified_at"] )

    # js_content is a list of dictionaries (even if just one)
    return js_content[0]
