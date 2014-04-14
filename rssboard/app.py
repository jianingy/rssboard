#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from rssboard.admin import feedadmin, useradmin
from rssboard.extensions import db, db_admin, admin
from rssboard.frontend import frontend
from rssboard.api import v1_api
from rssboard import filters

from flask import Flask
from oslo.config import cfg

application_opts = [
    cfg.BoolOpt('debug', default=False, help='Enable debug mode'),
]

CONF = cfg.CONF
CONF.register_cli_opts(application_opts)
CONF.register_opts(application_opts)


def make_frontend_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = CONF.database.connection

    filters.init_app(app)
    db.init_app(app)
    db_admin.init_app(app)
    admin.init_app(app)

    app.register_blueprint(frontend)
    app.register_blueprint(v1_api, url_prefix='/api/v1')

    admin.add_view(feedadmin)
    admin.add_view(useradmin)

    return app
