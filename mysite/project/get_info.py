#!/usr/bin/env python2.7

import urllib
from bs4 import BeautifulSoup as soup
import sqlite3
import string
import unicodedata
import requests

def remove_accents(data):
    # From https://stackoverflow.com/questions/8694815/removing-accent-and-special-characters#8695067
    line = data.split()
    for i, word in enumerate(line):
        line[i] = ''.join(x for x in unicodedata.normalize('NFKD', word) if x in string.ascii_letters).lower()
    return ' '.join(line)

def name_to_id(name):
    '''
    Currently not using...
    '''
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

    # for row in c.execute('SELECT * FROM anime'):
    #     # print row[0]
    #     # print type(row[0])
    #     if row[0] == name1:
    #         return int(row[1])

    # for row in c.execute('SELECT id FROM anime WHERE id =*?*', t):


def get_anime_info(name):
    name1 = name.encode('utf-8')
    name1 = name1.lower().strip()
    conn = sqlite3.connect('project/title_database.db')
    conn.text_factory = str
    descriptions = []
    c = conn.cursor()
    ids = []
    t = (name1, )

    # t = (name1, )
    # c.execute('SELECT id FROM anime WHERE title=?', t)
    # _id = str(c.fetchone()[0])

    for row in c.execute('SELECT * FROM anime'):
        x = str(row[0])
        if (name1 in x) or name1 == x.lower():
            ids.append(str(row[1]))

    # c.execute('SELECT id FROM anime WHERE id =*?', t)
    # ids.append(str(c.fetchall()))


    for _id in ids:
        bad = False
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
#TODO Add in more functionality-> website links, episode lists, run years,
# episode names,
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
            title = remove_accents(title).strip()
            title = item.text.encode('utf-8')
        crunchy = "-".join(title.split())
        URL = "https://www.crunchyroll.com/" + crunchy
        r = requests.get(url = URL)

        # print pic
        # print genres
        # print themes-
        # print songs
        # print plot_summary
        # print run_dates
        for show in descriptions: # Removes duplicate listings
            if show['title'] == title:
                bad = True
        if not bad:
            if r.ok:
                descriptions.append({'crunchy': crunchy, 'image': pic, 'title':title, 'genres': genres, 'themes': themes, 'songs': songs, 'summary': plot_summary})
            else:
                descriptions.append({'crunchy': None, 'image': pic, 'title':title, 'genres': genres, 'themes': themes, 'songs': songs, 'summary': plot_summary})
    print descriptions
    return descriptions
#for item in page_soup.findAll("item"):

 #       print item.find("Genres")


if  __name__=='__main__':
    get_anime_info("13")
