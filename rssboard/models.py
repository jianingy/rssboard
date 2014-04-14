#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#

from rssboard.extensions import db
from rssboard.utils import ModelIterableMixin
from rssboard.utils import utcnow

from sqlalchemy.ext import declarative


class HasIdMixin(object):
    id = db.Column(db.Integer, primary_key=True)


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, default=utcnow)
    updated_at = db.Column(db.DateTime, onupdate=utcnow)


class BASE(ModelIterableMixin):

    @declarative.declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'


class User(BASE, db.Model, HasIdMixin):

    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


class Feed(BASE, db.Model, HasIdMixin):

    name = db.Column(db.String(60), nullable=False, unique=True)
    source = db.Column(db.String(240), nullable=False)
    scheme = db.Column(db.Enum('rss',))

    def __repr__(self):
        return '<Feed %r:%r>' % (self.name, self.source)


class Post(BASE, db.Model, HasIdMixin, TimestampMixin):

    title = db.Column(db.String(60), nullable=False, unique=True)
    author = db.Column(db.String(240), nullable=True)
    link = db.Column(db.String(240), nullable=True)
    summary = db.Column(db.String(240))
    content = db.Column(db.Text, nullable=True)
    content_type = db.Column(db.String(60), default='text/html', nullable=True)
    posted_at = db.Column(db.DateTime, default=utcnow, nullable=False)

    visit = db.Column(db.Integer, nullable=False, default=0)
    up = db.Column(db.Integer, nullable=False, default=0)
    down = db.Column(db.Integer, nullable=False, default=0)

    feed_id = db.Column(db.Integer, db.ForeignKey('feeds.id'))
    feed = db.relationship('Feed', backref=db.backref('posts'))
