from mongoengine.fields import DateTimeField, ObjectIdField
import datetime
from mamigot.api import db


class Post(object):
    created_at  = db.DateTimeField(default=datetime.datetime.now, required=True)
    modified_at = db.DateTimeField(default=datetime.datetime.now, required=True)

    title = db.StringField(max_length=255, required=True)
    slug  = db.StringField(max_length=255, required=True)
    desc  = db.StringField(required=True)

    meta = {
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at'],
    }

    @classmethod
    def get_required_fields(cls):
        if issubclass(cls, db.Document):
            return [k for k,v in cls._fields.iteritems() if v.required]

        else: raise NotImplementedError

    @classmethod
    def get_manual_fields(cls):
        if issubclass(cls, db.Document):
            excluded_types = [DateTimeField, ObjectIdField]

            return [k for k,v in cls._fields.iteritems()
                    if type(v) not in excluded_types]

        else: raise NotImplementedError


class BlogPost(db.Document, Post):
    body  = db.StringField(required=True)


class ProjectPost(db.Document, Post):
    body  = db.StringField(required=True)
    highlighted = db.BooleanField(required=True)


class Image(db.Document, Post):
    image_url = db.StringField(required=True, max_length=255)
