# -*- coding: utf-8 -*-
import os
from datetime import timedelta

import jinja2
from flask import Flask
from flask import url_for
from flask.ext.bootstrap import Bootstrap

from .db import db
from .db import models
from .views.home import HomeView
from .views.unobtrusive import UnobtrusiveView


def custom_jinja2_filters(app):
    @app.template_filter('human_duration')
    def human_duration(millis):
        td = timedelta(milliseconds=millis)
        return str(td)

    @app.template_filter('human_price')
    def human_price(price):
        return '$ {0:.2f}'.format(price)


def paged_list_helper(app):
    from pagedlist.web import builder

    @app.context_processor
    def utility_processor():
        from pagedlist.web import options

        def paged_list_pager(paged_list, page_url_generator, options=None):
            return jinja2.Markup(builder.Builder.paged_list_pager(
                paged_list, page_url_generator, options))

        def page_url_generator(endpoint):
            return lambda page: url_for(endpoint, page=page)

        return dict(paged_list_pager=paged_list_pager,
                    page_url_generator=page_url_generator,
                    paged_options=options)


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
    UnobtrusiveView.register(app)
    # Bootstrap
    Bootstrap(app)
    # Helpers
    custom_jinja2_filters(app)
    paged_list_helper(app)
    return app
