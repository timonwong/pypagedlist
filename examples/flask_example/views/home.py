# -*- coding: utf-8 -*-
from flask import render_template
from flask.ext.classy import FlaskView


class HomeView(FlaskView):
    def index(self):
        return render_template('home/index.html')
