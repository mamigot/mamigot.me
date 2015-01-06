from flask import Response, request, json, jsonify
from flask.views import MethodView
import datetime
from mamigot.api.models import Post, BlogPost, ProjectPost, Image


class PostAPI(MethodView):
    model = Post

    @classmethod
    def get(cls, slug=None):
        if slug:
            data = cls.model.objects(slug=slug)
        else:
            data = cls.model.objects.all()

        if not data: return cls.resp(404)

        specific_fields = request.args.get('fields')
        if specific_fields:
            wanted = specific_fields.split(",")
            allowed = cls.model.get_required_fields()
            filtered = [w for w in wanted if w in allowed]

            if filtered:
                data = data.only(*filtered)

            else: return cls.resp(400)

        limit = request.args.get('limit')
        if limit and limit > 0:
            data = data[:int(limit)] # Only the first 'limit' results

        return cls.resp(200, data.to_json())


    @classmethod
    def post(cls):
        if not request.data: return cls.resp(400)
        data = json.loads(request.data)

        try:
            fields = cls.model.get_manual_fields()
            content = {f:data[f] for f in fields}

            cls.model(**content).save()
            return cls.resp(200)

        except KeyError, e:
            return cls.resp(400)


    @classmethod
    def put(cls): # At least requires 'slug' field
        if not request.data: return cls.resp(400)
        data = json.loads(request.data)

        if 'slug' not in data.keys():
            return cls.resp(400)

        else:
            post = cls.model.objects(slug=data['slug'])
            if post:
                fields = cls.model.get_manual_fields()

                content = {f:data[f] for f in data if f in fields}
                content['modified_at'] = datetime.datetime.now()

                # Bug: https://github.com/MongoEngine/mongoengine/issues/843
                fmtted = { ("set__" + k):v for k,v in content.iteritems() }

                post.update(**fmtted)
                return cls.resp(200)

            else:
                return cls.resp(404)


    @classmethod
    def delete(cls, slug=None):
        if not slug:
            return cls.resp(400)

        else:
            post = cls.model.objects(slug=slug)
            if post:
                post.delete()
                return cls.resp(200)

            else:
                return cls.resp(404)


    @staticmethod
    def resp(status, output_json=None):
        output_json = output_json if output_json else ""

        return Response(output_json, status=status, mimetype='application/json')


class BlogPostAPI(PostAPI):
    model = BlogPost


class ProjectPostAPI(PostAPI):
    model = ProjectPost


class ImageAPI(PostAPI):
    model = Image
