#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from rssboard.app import make_frontend_app

from oslo.config import cfg
from werkzeug.serving import run_simple
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.debug import DebuggedApplication


import logging
import os
import sys

CONF = cfg.CONF


def run_frontend():
    CONF(sys.argv[1:], project='rssboard')

    if CONF.debug:
        logging.basicConfig(level=logging.DEBUG)

    app = make_frontend_app()

    if CONF.debug:
        app.debug = CONF.debug
        app = DebuggedApplication(app, evalex=True)

    app = SharedDataMiddleware(app, {
        '/static': os.path.join(os.path.dirname(__file__), 'static')
        })

    run_simple('localhost', 8080, app, use_reloader=CONF.debug)


def add_cli_parsers(subparsers):
    subparsers.add_parser('renew', help="Renew all RSS Feed")


def run_manage():
    CONF.register_cli_opt(
        cfg.SubCommandOpt('action',
                          help='command to run',
                          handler=add_cli_parsers))

    CONF(sys.argv[1:], project='rssboard')

    if CONF.debug:
        logging.basicConfig(level=logging.DEBUG)

    from cli import renew_feed

    if CONF.action.name == 'renew':
        with make_frontend_app().app_context():
            renew_feed()
