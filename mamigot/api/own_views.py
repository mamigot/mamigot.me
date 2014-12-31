from flask import Response, request
from flask.views import MethodView
from mamigot.models import BlogPost


class BlogPostAPI(MethodView):

    def get_context(self, slug):
        post = BlogPost.objects.get_or_404(slug=slug)
        return post


    def get(self, slug=None):
        if slug:
            # Get specific post (in Blog collection, where slug = slug)
            msg = "getted - specified slug is " + slug
            return Response(msg, status=200, mimetype='application/json')

        else:
            # Get all posts
            msg =  "getted - (not specified)"
            return Response(msg, status=200, mimetype='application/json')


    def post(self):
        # Create post
        return Response("posted", status=200, mimetype='application/json')


    def put(self, slug):
        # Update post
        return Response("putted", status=200, mimetype='application/json')


    def delete(self, slug):
        # Delete post
        return Response("delete", status=200, mimetype='application/json')
