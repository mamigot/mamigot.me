from flask import Response, request, json, jsonify
from flask.views import MethodView
from mamigot.models import BlogPost


class BlogPostAPI(MethodView):

    def get(self, slug=None):
        if slug:
            post = BlogPost.objects(slug=slug)
            if post:
                return BlogPostAPI.return_200(post.to_json())

            else:
                return BlogPostAPI.abort_404(param_name='slug', param_value=slug)

        else:
            posts = BlogPost.objects.all()
            return BlogPostAPI.return_200(posts.to_json())


    def post(self):
        # Create post
        pass


    def put(self, slug):
        # Update post
        pass


    def delete(self, slug):
        # Delete post
        pass


    @staticmethod
    def return_200(output_json):
        return Response(output_json, status=200, mimetype='application/json')


    @staticmethod
    def abort_404(param_name, param_value):
        msg = "Error: no matches found for '%s' = '%s'." \
              % (param_name, param_value)

        resp = jsonify({ "message"  : msg })
        resp.status_code = 404
        return resp
