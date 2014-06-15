# -*- coding: utf-8 -*-
import math
import os

from flask import Flask
from flask import url_for
from flask.ext.bootstrap import Bootstrap
import jinja2

from .db import db
from .db import models
from .views.home import HomeView


def custom_jinja2_filters(app):
    @app.template_filter('human_size')
    def human_size(size):
        """http://stackoverflow.com/a/14822210"""
        size_name = ("KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size,1024)))
        p = math.pow(1024,i)
        s = round(size/p,2)
        if (s > 0):
           return '%s %s' % (s,size_name[i])
        else:
           return '0B'

    @app.template_filter('price')
    def price(price):
        return '$ {0:.2f}'.format(price)


def paged_list_helper(app):
    from pagedlist.web import builder

    @app.context_processor
    def utility_processor():
        def paged_list_pager(paged_list, page_url_generator, options=None):
            return jinja2.Markup(builder.Builder.paged_list_pager(
                paged_list, page_url_generator, options))

        def page_url_generator(endpoint):
            return lambda page: url_for(endpoint, page=page)

        return dict(paged_list_pager=paged_list_pager,
                    page_url_generator=page_url_generator)


def create_app():
    app = Flask(__name__)

    db_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'data', 'database.db'
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_path

    # SQLAlchemy
    db.app = app
    db.init_app(app)
    # Register views
    HomeView.register(app)
    # Bootstrap
    Bootstrap(app)
    # Helpers
    custom_jinja2_filters(app)
    paged_list_helper(app)
    return app
