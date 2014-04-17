#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#

from oslo.config import cfg

database_opts = [
    cfg.StrOpt('connection',
               default='sqlite:///rssboard.db',
               help='The database connection string'),
]

CONF = cfg.CONF
CONF.register_cli_opts(database_opts, 'database')
CONF.register_opts(database_opts, 'database')


from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(session_options={'autocommit': True})
db_admin = SQLAlchemy(session_options={'autocommit': False})


from flask.ext.admin import Admin
admin = Admin()
