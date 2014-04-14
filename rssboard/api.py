#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from rssboard.extensions import db
from rssboard.models import Feed
from rssboard.utils import jsonify

import flask

v1_api = flask.Blueprint('v1_api', __name__)


@v1_api.route('/feeds', methods=['GET'])
@jsonify
def list_feed():
    with db.session.begin(subtransactions=True):
        items = db.session.query(Feed).all()
        return map(lambda x: dict(x), items)


@v1_api.route('/feeds/<pk>', methods=['GET'])
@jsonify
def show_feed(pk):
    with db.session.begin(subtransactions=True):
        item = db.session.query(Feed).filter(Feed.id == pk).one()
        return dict(item)
