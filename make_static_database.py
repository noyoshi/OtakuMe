#!/usr/bin/env python2.7


import urllib
from bs4 import BeautifulSoup as soup
import sqlite3
import string
import unicodedata

def remove_accents(data):
    # From https://stackoverflow.com/questions/8694815/removing-accent-and-special-characters#8695067
    line = data.split()
    for i, word in enumerate(line):
        line[i] = ''.join(x for x in unicodedata.normalize('NFKD', word) if x in string.ascii_letters).lower()
    return ' '.join(line)

def parse_name(name):
    name = remove_accents(name)
    return name.encode('utf-8').lower()

def get_titles(_type):
    # This gets info on all anime in the list, around 82k titles?
    # url = "https://www.animenewsnetwork.com/encyclopedia/reports.xml?id=155&type=anime&nlist=all"
    url = "https://www.animenewsnetwork.com/encyclopedia/reports.xml?id=155&type=" + _type + "&nlist=all"

    client = urllib.urlopen(url)
    html = client.read()
    client.close()

    # Page is encoded in xml
    page_soup = soup(html, 'xml')

    titles = []
    d = {}

    for item in page_soup.findAll("item"):
        titles.append(parse_name(item.find("name").text))
        temp = [item.find("id").text.encode('utf-8'),
                item.find("gid").text.encode('utf-8')]
        d[titles[len(titles)-1]] = temp

    return titles, d

def make_database(titles, d, _type):
    # For details see https://docs.python.org/2/library/sqlite3.html
    if _type == 'anime':
        conn = sqlite3.connect('mysite/project/title_database.db')
        # conn = sqlite3.connect('data/title_database.db')

        conn.text_factory = str
        c = conn.cursor()
        c.execute('''CREATE TABLE anime
            (title text, id mediumint, gid INT)''')

        z = []

        for title in titles:
            # Tuples, since that is what SQLite3 uses
            z.append((title, d[title][0], d[title][1]))

        #print anime
        c.executemany('INSERT INTO anime VALUES (?,?,?)', z)
        # Making sure that that database was made correctly
        for row in c.execute('SELECT * FROM anime'):
            print row
        conn.commit()
        conn.close()
    elif _type == 'manga':
        conn = sqlite3.connect('mysite/project/manga_database.db')
        # conn = sqlite3.connect('data/title_database.db')

        conn.text_factory = str
        c = conn.cursor()
        c.execute('''CREATE TABLE manga
            (title text, id mediumint, gid INT)''')

        z = []

        for title in titles:
            # Tuples, since that is what SQLite3 uses
            z.append((title, d[title][0], d[title][1]))

        #print anime
        c.executemany('INSERT INTO manga VALUES (?,?,?)', z)
        # Making sure that that database was made correctly
        for row in c.execute('SELECT * FROM manga'):
            print row
        conn.commit()
        conn.close()


if __name__ == '__main__':
    # Creates the database
    # anime_titles, anime_d = get_anime_titles('anime')
    manga_titles, manga_d = get_titles('manga')

    # for title in anime_titles:
    #     print title, anime_d[title]
    for title in manga_titles:
        print title, manga_d[title]

    # make_database(titles, anime_d, 'anime')
    make_database(manga_titles, manga_d, 'manga')
