#!/usr/bin/env python2.7

'''
Using the api from animenewsnetwork.com:
    https://www.animenewsnetwork.com/encyclopedia/api.php
'''

import urllib
from bs4 import BeautifulSoup as soup
import sqlite3
import string
import unicodedata
