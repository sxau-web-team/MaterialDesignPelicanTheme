#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'admin'
SITENAME = u'独步清风\'s blog'
SITEURL = 'http://dbqf.xyz'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_RSS = u"feeds/all.rss.xml"
CATEGORY_FEED_RSS=u"feeds/%s.rss.xml"
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Changyanlong', 'http://getpelican.com/'),
         ('1433', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('', '#'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/dubuqingfeng'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Theme
THEME = 'pelican-themes/yeti'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DISQUS_SITENAME = u"dubuqingfeng"
GITHUB_USER = u"dubuqingfeng"
GITHUB_REPO_COUNT= 5
GITHUB_SKIP_FORK= False
GITHUB_SHOW_USER_LINK= False

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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
