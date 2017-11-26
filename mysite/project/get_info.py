#!/usr/bin/env python2.7

import urllib
from bs4 import BeautifulSoup as soup
import sqlite3
import string
import unicodedata


def name_to_id(name):
    name1 = name.encode('utf-8')
    print type(name1)
    conn = sqlite3.connect('project/title_database.db')
    conn.text_factory = str

    c = conn.cursor()
    t = (name, )
    # c.execute('SELECT id FROM anime WHERE id=?', t)
    # print c.fetchone()
    # return c.fetchone().encode('utf-8')

    # c.execute('SELECT id FROM anime WHERE title=?', t)
    # print c.fetchone()
    for row in c.execute('SELECT * FROM anime'):
        # print row[0]
        # print type(row[0])
        if row[0] == name1:
            return int(row[1])

def get_anime_info(name):
    name1 = name.encode('utf-8')
    name1 = name1.lower().strip()
    conn = sqlite3.connect('project/title_database.db')
    conn.text_factory = str

    c = conn.cursor()
    t = (name1, )
    c.execute('SELECT id FROM anime WHERE title=?', t)
    _id = str(c.fetchone()[0])
    url="https://www.animenewsnetwork.com/encyclopedia/api.xml?anime=" + _id

# TODO: MAKE IT POSSIBLE TO RETURN MULTIPLE THINGS PER search
# search:your -> your lie in april, your xx yy zz, etc
    client = urllib.urlopen(url)
    html = client.read()
    client.close()

    page_soup = soup(html, 'xml')

    genres = []
    themes = []
    songs = [[],[]] # op, ed
    run_dates = [] # Start, end
    plot_summary = ""
    pic = ""
    title = ""
    # for item in x:
    #     print item.text
    for item in page_soup.findAll(type="Ending Theme"):
        songs[1].append(item.text.encode('utf-8'))
    for item in page_soup.findAll(type="Opening Theme"):
        songs[0].append(item.text.encode('utf-8'))
    for item in page_soup.findAll(type="Plot Summary"):
        plot_summary = item.text.encode('utf-8')
    for item in page_soup.findAll(type="Genres"):
        genres.append(item.text.encode('utf-8'))
    for item in page_soup.findAll(type="Themes"):
        themes.append(item.text.encode('utf-8'))
    for item in page_soup.findAll(type="Vintage"):
        run_dates.append(item.text.encode('utf-8'))
    for item in page_soup.findAll(type="Picture"):
        pic= item.find('img')['src']
    for item in page_soup.findAll(type="Main title"):
        title = item.text.encode('utf-8')
    # print pic
    # print genres
    # print themes
    # print songs
    # print plot_summary
    # print run_dates
    return {'image': pic, 'title':title, 'genres': genres, 'themes': themes, 'songs': songs, 'summary': plot_summary}
#    for item in page_soup.findAll("item"):

 #       print item.find("Genres")


if  __name__=='__main__':
    get_anime_info("13")