#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#

from rssboard.services import post_service
from rssboard.utils import jsonify

from flask import request
import flask

v1_api = flask.Blueprint('v1_api', __name__)

# TODO: create a new decortator impl both routing and result encoding
# @route(v1_api, 'GET|POST|HEAD /posts')

@v1_api.route('/posts', methods=['GET'])
@jsonify
def list_post():
    order_by = request.args.get('order_by', 'recent')
    if order_by == 'recent':
        order_by = 'posted_at desc'
    elif order_by == 'best':
        order_by = 'up desc'
    elif order_by == 'worst':
        order_by = 'down desc'
    elif order_by == 'most':
        order_by = 'visit desc'
    return map(lambda x: dict(x), post_service.list(order_by=order_by))
