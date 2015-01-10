from mamigot.frontend import app
from views import index, blog, projects, resume_html, resume_pdf, ext_profile



app.add_url_rule('/', view_func = index)


app.add_url_rule('/blog/', view_func = blog)
app.add_url_rule('/blog/<string:slug>', view_func = blog)


app.add_url_rule('/projects/', view_func = projects)
app.add_url_rule('/projects/<string:slug>', view_func = projects)


app.add_url_rule('/resume/', view_func = resume_html)
app.add_url_rule('/resume/pdf/', view_func = resume_pdf)


app.add_url_rule('/profile/<string:site>/', view_func = ext_profile)
