#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianing.yang@qunar.com>
#
from .exceptions import CommonError
from .utils import boxquote

from functools import wraps
from flask import jsonify
from oslo.config import cfg
from traceback import format_exc

import logging

CONF = cfg.CONF
LOG = logging.getLogger(__name__)


class ClientError(CommonError):
    status_code = 400


def api_route(bp, rule, **options):
    options.setdefault('strict_slashes', False)

    methods, endpoint = rule.split(' ', 2)
    options['methods'] = methods.split('|')

    def decorator(f):
        @bp.route(endpoint, **options)
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                status_code = 200
                retval = f(*args, **kwargs)
                if isinstance(retval, tuple):
                    status_code = retval[1]
                    retval = retval[0]
                return jsonify(dict(data=retval)), status_code
            except ClientError as e:
                errmsg = dict(msg=unicode(e), code=e.errcode)
                if CONF.debug:
                    errmsg['traceback'] = format_exc()
                return jsonify(dict(error=errmsg)), e.status_code
            except Exception as e:
                errmsg = dict(msg=unicode(e))
                if CONF.debug:
                    errmsg['traceback'] = format_exc()
                LOG.warn('Exception: %s\n%s' % (e, boxquote('traceback',
                                                            format_exc())))
                return jsonify(dict(error=errmsg)), 500
        return f

    return decorator
