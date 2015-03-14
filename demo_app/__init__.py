from flask import Flask
from flask.ext.bootstrap import Bootstrap

from demo_app import configmodule


app = Flask(__name__)
app.config.from_pyfile('static/application.cfg', silent=False)

bootstrap = Bootstrap(app)

import demo_app.views
