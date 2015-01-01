from flask import Response, request, json, jsonify
from flask.views import MethodView
from mamigot.models import BlogPost


class BlogPostAPI(MethodView):

    def get(self, slug=None):
        if slug:
            post = BlogPost.objects(slug=slug)
            if post:
                return BlogPostAPI.resp(200, post.to_json())

            else:
                return BlogPostAPI.resp(404)

        else:
            posts = BlogPost.objects.all()
            return BlogPostAPI.resp(200, post.to_json())


    def post(self):
        data = request.data


    def put(self, slug):
        pass


    def delete(self, slug=None):
        if not slug:
            return BlogPostAPI.resp(400)

        else:
            post = BlogPost.objects(slug=slug)
            if post:
                post.delete()
                return BlogPostAPI.resp(200)

            else:
                return BlogPostAPI.resp(404)


    @staticmethod
    def resp(status, output_json=None):
        output_json = output_json if output_json else ""

        return Response(output_json, status=status, mimetype='application/json')
