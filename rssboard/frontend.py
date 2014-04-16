#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#

from rssboard.services import post_service

from flask import redirect, render_template, url_for
import flask

frontend = flask.Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return redirect(url_for('frontend.recent'), code=301)


@frontend.route('/recent')
def recent():
    posts = post_service.list(order_by='posted_at desc')
    return render_template("index.html", posts=posts)


@frontend.route('/best')
def best():
    posts = post_service.list(order_by='up desc')
    return render_template("index.html", posts=posts)


@frontend.route('/worst')
def worst():
    posts = post_service.list(order_by='down desc')
    return render_template("index.html", posts=posts)


@frontend.route('/most')
def most():
    posts = post_service.list(order_by='visit asc')
    return render_template("index.html", posts=posts)


@frontend.route('/redirect/<post_id>')
def redirect_with_accounting(post_id):
    link = post_service.visit(post_id)
    return redirect(link, code=302)


@frontend.route('/posts/<post_id>/up')
def vote_up(post_id):
    post_service.vote_up(post_id, 1)
    return redirect(url_for('frontend.index'), code=302)


@frontend.route('/posts/<post_id>/down')
def vote_down(post_id):
    post_service.vote_down(post_id, 1)
    return redirect(url_for('frontend.index'), code=302)
