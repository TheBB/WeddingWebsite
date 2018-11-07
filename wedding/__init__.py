from flask import render_template, Flask
import os


def about():
    return render_template('about.djhtml')

def index():
    return render_template('index.djhtml')

def place():
    return render_template('place.djhtml')

def schedule():
    return render_template('schedule.djhtml')

def info():
    return render_template('info.djhtml')

def news():
    return render_template('news.djhtml')

def moments():
    return render_template('moments.djhtml')


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        if 'WEDDING_CONFIG' in os.environ:
            app.config.from_envvar('WEDDING_CONFIG')
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.route('/')(index)
    app.route('/about')(about)
    app.route('/place')(place)
    app.route('/schedule')(schedule)
    app.route('/info')(info)
    app.route('/news')(news)
    app.route('/moments')(moments)

    return app
