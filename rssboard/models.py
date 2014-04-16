#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#

from rssboard.extensions import db as flask_db
from rssboard.common import db
from rssboard.common.timeutils import utcnow

import sqlalchemy as sa


class BASE(flask_db.Model, db.JSONSeriableMixin, db.TableNameMixin):

    __abstract__ = True


class User(BASE, db.HasIdMixin):

    email = sa.Column(sa.String(60), nullable=False, unique=True)
    password = sa.Column(sa.String(60), nullable=False)
    is_admin = sa.Column(sa.Boolean, default=False)


class Feed(BASE, db.HasIdMixin):

    name = sa.Column(sa.String(60), nullable=False, unique=True)
    source = sa.Column(sa.String(240), nullable=False)
    scheme = sa.Column(sa.Enum('rss',))

    def __repr__(self):
        return '<Feed %r:%r>' % (self.name, self.source)


class Post(BASE, db.HasIdMixin, db.TimestampMixin):

    title = sa.Column(sa.String(60), nullable=False, unique=True)
    author = sa.Column(sa.String(240), nullable=True)
    link = sa.Column(sa.String(240), nullable=True)
    summary = sa.Column(sa.String(240))
    content = sa.Column(sa.Text, nullable=True)
    content_type = sa.Column(sa.String(60), default='text/html', nullable=True)
    posted_at = sa.Column(sa.DateTime, default=utcnow, nullable=False)

    visit = sa.Column(sa.Integer, nullable=False, default=0)
    up = sa.Column(sa.Integer, nullable=False, default=0)
    down = sa.Column(sa.Integer, nullable=False, default=0)

    feed_id = sa.Column(sa.Integer, sa.ForeignKey('feeds.id'))
    feed = sa.orm.relationship('Feed', backref=sa.orm.backref('posts'))


class Comment(BASE, db.HasIdMixin, db.TimestampMixin):

    email = sa.Column(sa.String(60), nullable=False)
    content = sa.Column(sa.String(160), nullable=False)
    up = sa.Column(sa.Integer, nullable=False, default=0)
    down = sa.Column(sa.Integer, nullable=False, default=0)

    post_id = sa.Column(sa.Integer, sa.ForeignKey('posts.id'))
    post = sa.orm.relationship('Post', backref=sa.orm.backref('comments'))
