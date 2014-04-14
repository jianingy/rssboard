#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#

from rssboard.extensions import db_admin
from rssboard.models import Feed, User

from flask.ext.admin.contrib.sqla import ModelView
from wtforms import validators
import wtforms


class UserAdmin(ModelView):
    searchable_columns = ('email',)
    excluded_list_columns = ['password']
    list_columns = ('email', 'is_admin')
    form_columns = ('email', 'is_admin')

    def scaffold_form(self):
        form_class = super(UserAdmin, self).scaffold_form()
        form_class.password = wtforms.PasswordField('Password',
                                                    [validators.required()])
        return form_class

feedadmin = ModelView(Feed, db_admin.session)
useradmin = UserAdmin(User, db_admin.session)
