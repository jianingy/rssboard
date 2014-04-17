#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianing.yang@qunar.com>
#


class BaseService(object):

    __model__ = None

    def __init__(self, db):
        self.db = db

    def find(self, **criteria):
        return self.__model__.query.filter_by(**criteria)

    def first(self, **criteria):
        return self.find(**criteria).first()

    def list(self, **kwargs):
        q = self.__model__.query

        if 'start' in kwargs:
            q = q.offset(kwargs['start'])

        if 'count' in kwargs:
            q = q.limit(kwargs['count'])

        if 'order_by':
            q = q.order_by(kwargs['order_by'])

        return q.all()

    def one(self, **criteria):
        return self.find(**criteria).one()

    def save(self, model):
        self.db.session.add(model)
        return model
