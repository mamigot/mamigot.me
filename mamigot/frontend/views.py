from flask import request, render_template, redirect
import requests

from mamigot.frontend import api



def index():
    blog_posts = api.get_posts_list('blog', limit=3)
    projects = api.get_posts_list('projects', limit=3,
                                   addl_url_params = {"highlighted":"false"})

    return render_template('layouts/index.html',
                            blog_posts=blog_posts, project_posts=projects)


def blog_archive():
    blog_posts = api.get_posts_list('blog')

    return render_template('layouts/blog.html', blog_posts=blog_posts)


def blog_post(slug):
    try:
        post = api.get_single_post('blog', slug)

    except requests.exceptions.HTTPError:
        return render_template('errors/404.html')

    return render_template('layouts/blog-post.html', post=post)


def projects(slug=None):
    project_posts = api.get_posts_list('projects')

    if slug:
        try:
            post = api.get_single_post('projects', slug)

        except requests.exceptions.HTTPError:
            return render_template('errors/404.html')

    else: # If no slug is provided, focus on the first one
        post = api.get_single_post('projects', project_posts[0]['slug'])

    return render_template('layouts/projects.html', shown_post=post,
                            posts=project_posts)


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
