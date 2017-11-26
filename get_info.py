#!/usr/bin/env python2.7

import urllib
from bs4 import BeautifulSoup as soup
import sqlite3
import string
import unicodedata

def get_anime_info(_id):
    url="https://www.animenewsnetwork.com/encyclopedia/api.xml?anime=" + _id

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
