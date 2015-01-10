from flask import request, render_template, redirect
import requests

from mamigot.frontend import api



def index():
    blog = api.get_posts_list('blog', limit=3)
    projects = api.get_posts_list('projects', limit=3,
                                   addl_url_params = {"highlighted":"false"})

    return render_template('layouts/index.html',
                            blog_posts=blog, project_posts=projects)


def blog_archive():

    return render_template('layouts/blog.html')


def blog_post(slug):
    return render_template('layouts/blog.html')


def projects():
    return render_template('layouts/projects.html')


def project_post(slug):
    return render_template('layouts/projects.html')


def resume_html():
    return render_template('layouts/resume.html')


def resume_pdf():
    pass


def ext_profile(site):
    site = site.lower()

    if site == "linkedin":
        return redirect('https://linkedin.com/in/miguelamigotgonzalez/')

    elif site == "twitter":
        return redirect('https://twitter.com/miguelamigot')

    elif site == "github":
        return redirect('https://github.com/miguel5')

    elif site == "facebook":
        return redirect('https://facebook.com/m.amigot')

    else:
        return render_template('errors/404.html')
