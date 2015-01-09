from flask import request, render_template, redirect
import requests
import api



def index():
    blog_posts = api.get_posts_list('blog', 1)
    project_posts = api.get_posts_list('projects', 1)

    return render_template( 'layouts/index.html',
                            blog_posts=blog_posts, project_posts=project_posts)


def blog_archive():

    return render_template('layouts/blog.html')


def blog_post():
    return render_template('blog.html')


def projects():
    return render_template('projects.html')


def project_post():
    return render_template('projects.html')


def resume_html():
    return render_template('resume.html')


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
