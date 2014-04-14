#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 IT/CCOPS/OPSDEV, Qunar Inc. (qunar.com)
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#

from rssboard.extensions import db
from rssboard.models import Feed, Post

from datetime import datetime
from time import mktime
from sqlalchemy import func

import feedparser
import logging
import sqlalchemy.orm.exc as orm_exc

LOG = logging.getLogger(__name__)


def renew_feed():
    with db.session.begin(subtransactions=True):
        items = db.session.query(Feed).all()
        for item in items:
            if item.scheme in ('rss',):
                LOG.info('renew RSS Feed: %s(%s)' % (item.name, item.source))
                renew_rss_feed(item)


def renew_rss_feed(item):
    try:
        with db.session.begin(subtransactions=True):

            # find latest post of this feed
            try:
                model_query = db.session.query(func.max(Post.posted_at))
                latest = model_query.filter(Post.feed_id == item.id).one()
                latest = latest[0]
            except orm_exc.NoResultFound:
                latest = None

            d = feedparser.parse(item.source)
            for entry in d.entries:
                posted_at = datetime.fromtimestamp(
                    mktime(entry.updated_parsed))

                if latest and posted_at <= latest:
                    LOG.debug('Post "%s" is too old' % entry.title)
                    continue

                post = Post()
                post.feed_id = item.id
                post.author = entry.author
                post.title = entry.title
                post.summary = entry.summary
                post.link = entry.link
                post.content_type = entry.content[0].type
                post.content = entry.content[0].value
                post.posted_at = posted_at

                LOG.info('new post "%s" from %s' % (post.title, item.name))
                db.session.add(post)

    except Exception as e:
        raise e
