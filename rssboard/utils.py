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
import sqlalchemy.orm.exc as orm_exc


def jsonify(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            retval = f(*args, **kwargs)
            response = flask.make_response(json.dumps(retval))
            response.headers['Content-Type'] = 'application/json'
            return response
        except orm_exc.NoResultFound:
            return '', 404

    return wrapper


def utcnow():
    return datetime.datetime.utcnow()


class ModelIterableMixin(object):

    def __iter__(self):
        """ Returns a JSON representation of an SQLAlchemy-backed object.
        """

        for col in self._sa_class_manager.mapper.mapped_table.columns:
            yield (col.name, getattr(self, col.name))
