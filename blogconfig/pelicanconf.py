#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'dubuqingfeng'
SITENAME = u"\u72ec\u6b65\u6e05\u98ce's blog"
SITEURL = 'dubuqingfeng.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'cn'

# Feed generation is usually not desired when developing
FEED_RSS = u"feeds/all.rss.xml"
CATEGORY_FEED_RSS=u"feeds/%s.rss.xml"
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('1433', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('', '#'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/dubuqingfeng'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'pelican-themes/yeti'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DISQUS_SITENAME = u"dubuqingfeng"
GITHUB_USER = u"dubuqingfeng"

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Plugin
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'sitemap', 'gravatar' ]

# Sitemap
SITEMAP = {
    'format': 'xml',
        'priorities': {
'articles': 1,
    'pages': 0.9,
    'indexes': 0.8,
        },
            'changefreqs': {
'indexes': 'daily',
    'articles': 'daily',
    'pages': 'weekly'
    }
}