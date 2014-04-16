#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
import datetime
import flask
import functools
import json


def jsonify(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        retval = f(*args, **kwargs)
        response = flask.make_response(json.dumps(retval))
        response.headers['Content-Type'] = 'application/json'
        return response

    return wrapper
