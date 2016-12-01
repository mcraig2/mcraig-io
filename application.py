""" Welp. Here you go. """
from flask import Flask

def say_hello(username="world"):
    return '<p>Hello %s!</p>\n' % username

header_text = """
<html><head><title>Test</title></head><body>"""
footer_text = '</body></html>'

# EB looks for an 'application' callable by default
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text + \
                         say_hello() + footer_text))


if __name__ == '__main__':
    application.run()
