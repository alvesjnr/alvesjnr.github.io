#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Antonio Ribeiro'
SITENAME = u'My Blog, My Rules.'
SITEURL = 'http://alvesjnr.github.io'
DISQUS_SHORTNAME = 'myblogmyrules'

TIMEZONE = 'Europe/Paris'
THEME = 'templates/notmyidea'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['latex']

# Blogroll
LINKS =  (
          ('Python.org', 'http://python.org/'),
          ('Python Brasil', 'http://www.python.org.br/wiki'),
		  ('Pelican', 'http://getpelican.com/'),
		  )

# Social widget
SOCIAL = (('Github', 'http://www.github.com/alvesjnr'),
          ('Bitbucket', 'http://www.bitbucket.com/alvesjnr'),
          ('Facebook','http://www.facebook.com/alvesjnr'),
          ('Twitter','http://www.twitter.com/alvesjnr'),
          ('E-Mail','mailto:alvesjunior.antonio@gmail.com'))

DEFAULT_PAGINATION = False 

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
