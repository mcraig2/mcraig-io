""" Welp. Here you go. """
from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    application.run()
