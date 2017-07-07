""" Welp. Here you go. """
import markdown
from flask import Flask
from flask import render_template
from flask import Markup

import blog_util

application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/blog')
@application.route('/blog/<name>')
def blog(name=None):
    if name is None:
        names = blog_util.get_blog_names()
        return render_template('blog.html', names=names)

    # A specific blog was requested, so convert to HTML from markdown and serve
    # content = Markup(markdown.markdown(content_as_str))
    fname = 'templates/blog/{}.md'.format(name.lower().replace(' ', '-'))
    with open(fname, 'r') as f:
        content = Markup(markdown.markdown(''.join(f.readlines())))
    return render_template('base_blog.html',
                           post_title=name,
                           post_content=content)


if __name__ == '__main__':
    application.run()
