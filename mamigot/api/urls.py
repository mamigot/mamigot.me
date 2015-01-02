from mamigot.api import app
from views.own import BlogPostAPI, ProjectPostAPI, ImageAPI
from views.ext import linkedin, github


app.add_url_rule('/linkedin/<string:item>', view_func = linkedin)

app.add_url_rule('/github/<string:item>', view_func = github)



blog_post_view = BlogPostAPI.as_view('blog_post_api')

app.add_url_rule('/blog/posts/', view_func = blog_post_view)

app.add_url_rule('/blog/posts/<string:slug>', view_func = blog_post_view)


project_post_view = ProjectPostAPI.as_view('project_post_api')

app.add_url_rule('/projects/posts/', view_func = project_post_view)

app.add_url_rule('/projects/posts/<string:slug>', view_func = project_post_view)


image_view = ImageAPI.as_view('image_api')

app.add_url_rule('/images/', view_func = image_view)

app.add_url_rule('/images/<string:slug>', view_func = image_view)
