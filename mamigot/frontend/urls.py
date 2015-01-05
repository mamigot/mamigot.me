from mamigot import app


app.add_url_rule('/', view_func = main_page)


app.add_url_rule('/resume/', view_func = resume_html)
app.add_url_rule('/resume/pdf/' + url_date, view_func = resume_pdf)


app.add_url_rule('/projects', view_func = projects_archive)
app.add_url_rule('/projects/<string:slug>', view_func = project_post)


app.add_url_rule('/blog', view_func = blog_archive)
app.add_url_rule('/blog/<int:year>/<int:month>/<int:day>/<string:slug>',
                 view_func = blog_post)
