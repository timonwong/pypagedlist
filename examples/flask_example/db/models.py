# -*- coding: utf-8 -*-
from . import sa


class Track(sa.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Unicode(200))
    composer = sa.Column(sa.Unicode(220))
    duration = sa.Column(sa.Integer)
    size = sa.Column(sa.Integer)
    unit_price = sa.Column(sa.Numeric(precision=10, scale=2))
