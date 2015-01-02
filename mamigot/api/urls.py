from mamigot.api import app
from views.ext import linkedin, github
from views.own import BlogPostAPI


app.add_url_rule('/linkedin/<string:item>', view_func = linkedin)

app.add_url_rule('/github/<string:item>', view_func = github)



blog_post_view = BlogPostAPI.as_view('blog_post_api')

app.add_url_rule('/blog/posts/', view_func = blog_post_view)

app.add_url_rule('/blog/posts/<string:slug>', view_func = blog_post_view)
