#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianing.yang@qunar.com>
#
from rssboard.common.service import BaseService
from rssboard.extensions import db
from rssboard.models import Post


class PostService(BaseService):

    __model__ = Post

    def vote_up(self, post_id, count):
        with db.session.begin(subtransactions=True):
            post = self.one(id=post_id)
            post.up = post.up + count
            self.save(post)
            return post.up

    def vote_down(self, post_id, count):
        with db.session.begin(subtransactions=True):
            post = self.one(id=post_id)
            post.down = post.down + count
            self.save(post)
            return post.down

    def visit(self, post_id):
        with db.session.begin(subtransactions=True):
            post = self.one(id=post_id)
            post.visit = post.visit + 1
            return post.link


post_service = PostService(db)
