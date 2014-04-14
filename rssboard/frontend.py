#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from rssboard.extensions import db
from rssboard.models import Post

from flask import redirect, render_template, url_for

import flask
import sqlalchemy.orm.exc as orm_exc

frontend = flask.Blueprint('frontend', __name__)
LIMIT = 50

@frontend.route('/')
def index():
    return redirect(url_for('frontend.recent'), code=301)


@frontend.route('/recent')
def recent():
    with db.session.begin(subtransactions=True):
        q = db.session.query(Post).order_by(Post.posted_at.desc()).limit(LIMIT)
        posts = q.all()
        return render_template("index.html", posts=posts)


@frontend.route('/best')
def best():
    with db.session.begin(subtransactions=True):
        q = db.session.query(Post).order_by(Post.up.desc()).limit(LIMIT)
        posts = q.all()
        return render_template("index.html", posts=posts)


@frontend.route('/worst')
def worst():
    with db.session.begin(subtransactions=True):
        q = db.session.query(Post).order_by(Post.down.desc()).limit(LIMIT)
        posts = q.all()
        return render_template("index.html", posts=posts)


@frontend.route('/most')
def most():
    with db.session.begin(subtransactions=True):
        q = db.session.query(Post).order_by(Post.visit.desc()).limit(LIMIT)
        posts = q.all()
        return render_template("index.html", posts=posts)


@frontend.route('/redirect/<post_id>')
def redirect_with_accounting(post_id):
    try:
        with db.session.begin(subtransactions=True):
            post = db.session.query(Post).filter(Post.id == post_id).one()
            post.visit = post.visit + 1
            return redirect(post.link, code=302)
    except orm_exc.NoResultFound:
        return 'Post not found', 404


@frontend.route('/posts/<post_id>/up')
def vote_up(post_id):
    try:
        with db.session.begin(subtransactions=True):
            post = db.session.query(Post).filter(Post.id == post_id).one()
            post.up = post.up + 1
            return redirect(url_for('frontend.index'), code=302)
    except orm_exc.NoResultFound:
        return 'Post not found', 404


@frontend.route('/posts/<post_id>/down')
def vote_down(post_id):
    try:
        with db.session.begin(subtransactions=True):
            post = db.session.query(Post).filter(Post.id == post_id).one()
            post.down = post.down + 1
            return redirect(url_for('frontend.index'), code=302)
    except orm_exc.NoResultFound:
        return 'Post not found', 404
