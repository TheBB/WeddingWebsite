from flask import render_template, Flask, request
import os
import json
from datetime import datetime
import hashlib


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

def rsvp():
    if 'submit' not in request.form:
        return render_template('rsvp.djhtml')

    data = dict(request.form.items())
    del data['submit']
    data['timestamp'] = str(datetime.now())
    data = json.dumps(data).encode('utf-8')

    h = hashlib.sha1()
    h.update(data)
    filename = h.hexdigest() + '.json'

    with open(os.path.join('responses', filename), 'wb') as f:
        f.write(data)
    return render_template('rsvp.djhtml', msg=True)


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
    app.route('/rsvp', methods=['GET', 'POST'])(rsvp)

    return app
