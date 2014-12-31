''' GENERATE TEST DATA FOR THE DATABASE '''
import sys
sys.path.append('/Users/miguelamigot/Software/GitHub/mamigot.me/')
sys.path.append('/Users/miguelamigot/Software/GitHub/mamigot.me/mamigot/')

from mongoengine import connect
connect('mamigot_test')

from models import BlogPost, ProjectPost, Image


def emptyDB():
    BlogPost.objects.all().delete()
    ProjectPost.objects.all().delete()
    Image.objects.all().delete()


emptyDB()

for i in range(5):
    vals = {"title" : "title" + str(i),
            "slug"  : "slug" + str(i),
            "desc"  : "desc" + str(i),
            }

    BlogPost(body="body" + str(i), **vals).save()
    ProjectPost(body="body" + str(i), **vals).save()
    Image(image_url="url" + str(i), **vals).save()
