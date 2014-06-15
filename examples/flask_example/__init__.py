# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from .db import sa
from .views.home import HomeView



def create_app():
    app = Flask(__name__)

    db_path = os.path.join(
        os.path.dirname(os.path.abspath(__name__)),
        'data', 'database.db'
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_path
    # SQLAlchemy
    sa.init_app(app)
    # Register views
    HomeView.register(app, route_base='/')
    # Bootstrap
    Bootstrap(app)

    return app
