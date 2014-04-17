#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianing.yang@qunar.com>
#


class CommonError(Exception):

    message = "An unknown exception occurred."
    errcode = -1

    def __init__(self, **kwargs):
        super(CommonError, self).__init__(self.message % kwargs)
        self.msg = self.message % kwargs

    def __unicode__(self):
        return unicode(self.msg)

    def use_fatal_exceptions(self):
        return False
