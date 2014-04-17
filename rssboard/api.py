#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#

from rssboard.common.api import api_route, ClientError
from rssboard.services import post_service


from flask import request
import flask

v1_api = flask.Blueprint('v1_api', __name__)


@api_route(v1_api, 'GET /posts')
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
    posts = post_service.list(order_by=order_by)
    return map(lambda x: dict(x), posts)
