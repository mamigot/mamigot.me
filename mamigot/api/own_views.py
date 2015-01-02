from flask import Response, request, json, jsonify
from flask.views import MethodView
import datetime
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
            return BlogPostAPI.resp(200, posts.to_json())


    def post(self):
        data = json.loads(request.data)

        try:
            fields = BlogPost.get_required_fields()

            content = {f:data[f] for f in fields}
            content['modified_at'] = datetime.datetime.now()

            BlogPost(**content).save()
            return BlogPostAPI.resp(200)

        except KeyError, e:
            return BlogPostAPI.resp(400)


    def put(self): # At least requires 'slug' field
        data = json.loads(request.data)

        if 'slug' not in data.keys():
            return BlogPostAPI.resp(400)

        else:
            post = BlogPost.objects(slug=slug)
            if post:
                fields = BlogPost.get_required_fields()

                content = {f:data[f] for f in data if f in fields}
                content['modified_at'] = datetime.datetime.now()

                post.update(**content)
                return BlogPostAPI.resp(200)

            else:
                return BlogPostAPI.resp(404)


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
