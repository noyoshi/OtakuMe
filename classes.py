
#!/usr/bin/env python2.7

'''
Using the api from animenewsnetwork.com:
    https://www.animenewsnetwork.com/encyclopedia/api.php

Class query holds informatin for whatever a user searches, and saves that data
to a static cache.

Sub classes anime / manga are made due to the popularity of both genres.
Anime class will hold links to *legal* streams, and manga class will hold
links to *legaL* translations, as well as places to purchase it from. It will
necessarily contain the ISBN number of the book (or the first book in the series)
'''

class query(object):
    def __init__(self, title, _id, author=None, description=None, related=None):

        self.title = title
        self.id = _id
        self.author = author
        self.description = description # A description of the work
        self.related = related # A list of related works, [[title, id]..]

    def get_title(self):
        return self.title

    def get_id(self):
        return self.id

    def get_author(self):
        return self.author

    def get_description(self):
        return self.description

    def get_related(self):
        return self.related

class anime(query):
    def __init__(self, streams=None):
        self.streams = streams

    def get_streams(self):
        return self.streams

class manga(query):
    def __init__(self, readers=None, isbn=None):
        self.readers = readers # List of URLS
        self.isbn = isbn # ISBN Number

    def get_readers(self):
        return self.readers

    def get_isbn(self):
        return self.isbn
