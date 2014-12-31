import datetime
from mamigot import db


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


class BlogPost(db.Document, Post):
    body  = db.StringField(required=True)


class ProjectPost(db.Document, Post):
    body  = db.StringField(required=True)


class Image(db.Document, Post):
    image_url = db.StringField(required=True, max_length=255)
