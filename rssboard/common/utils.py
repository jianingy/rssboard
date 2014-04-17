#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianing.yang@qunar.com>
#


def boxquote(title, body):
    length = 78
    padding = '=' * ((length - len(title)) / 2)
    top = '%s %s %s' % (padding, title, padding)
    bottom = '^' * length
    return '%s\n%s\n%s' % (top[:length], body, bottom)
