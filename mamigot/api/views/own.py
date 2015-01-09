from flask import Response, request, json, jsonify
from flask.views import MethodView

from mongoengine.fields import DateTimeField
import datetime, json

from mamigot.api.models import Post, BlogPost, ProjectPost, Image


class PostAPI(MethodView):
    model = Post

    @classmethod
    def find(cls, slug=None):
        if slug:
            data = cls.model.objects(slug=slug)
        else:
            data = cls.model.objects.all()

        return data


    @classmethod
    def get(cls, slug=None):
        qset = cls.find(slug)
        if not qset: return cls.resp(404)

        # Get only the fields that were specified in the URLs
        specific_fields = request.args.get('fields')
        if specific_fields:
            wanted = specific_fields.split(",")
            allowed = cls.model.get_required_fields()

            chosen_fields = [w for w in wanted if w in allowed]
            if chosen_fields:
                qset = qset.only(*chosen_fields)

            else: return cls.resp(400)

        # Limit the number of results
        limit = request.args.get('limit')
        if limit and limit > 0:
            qset = qset[:int(limit)] # Only the first 'limit' results


        js_resp = cls.clean_output(qset)
        return cls.resp(200, js_resp)


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


    @classmethod
    def clean_output(cls, qset):
        '''
        Cleans a queryset (returned value from Mongo) and returns as JSON
        '''
        qset = qset.exclude("id")

        # Format dates (currently are timestamps)
        # http://stackoverflow.com/questions/13230284/convert-mongodb-return-object-to-dictionary
        # http://api.mongodb.org/python/current/api/bson/son.html
        props = [ob.to_mongo().to_dict() for ob in qset]

        ''' RETURN CLEAN OUTPUT '''

        return json.dumps( [{"":""}] )


    @staticmethod
    def resp(status, output_json=None):
        output_json = output_json if output_json else ""

        return Response(output_json, status=status, mimetype='application/json')


class BlogPostAPI(PostAPI):
    model = BlogPost


class ProjectPostAPI(PostAPI):
    model = ProjectPost

    @classmethod
    def find(cls, slug=None):
        data = super(ProjectPostAPI, cls).find(slug)

        # Apply specific filtering
        if request.args.get('highlighted') == 'true':
            data = data.filter(highlighted=True)

        return data


class ImageAPI(PostAPI):
    model = Image
