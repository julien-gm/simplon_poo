import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from requests import get
import requests
import json

class Album:
    title:str
    author:str
    year:int
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def __str__(self):
        return f"{self.author}:{self.title} ({self.year})"

def scrap_album(artist):
    albums=[]
    url = requests.get(f"https://www.allformusic.fr/{artist}/discographie")
    soup = BeautifulSoup(url.content, "html5lib")
    id = soup.find(id="disco-album")
    alldiv = id.find_all("div")

    for disco in alldiv:
        albums.append(Album(disco.strong.get_text(), artist,int(disco.span.get_text()[-4:])))
    return albums

discography= []
albums = []
artist=["jamiroquai", "daft-punk", "justice"]

for i in artist:
    albums+= scrap_album(i)

for i in albums:
    jsonString = (i.__dict__)
    discography.append(jsonString)

with open('discography.json', 'w') as a:
    json.dump(discography, a, indent=8)
    print("JSON file created")

class AlbumRepository:
    albums_list = []
    
    def __init__(self, albums):
        self.albums = albums
        
    def get_albums(self):
        print(self.albums)

    def add_album(self, albums):
        self.albums_list.append(Album(**albums))
        print ("The album is added")

    def delete_album(self, albums):
        for albums in self.albums_list:
            if albums.title == albums['title']:
                self.albums_list.remove(albums)
        print ("The album is deleted")

    def modify_album(self,albums,update):
        for albums in self.albums:
            if albums.title == albums['title']:
                albums.title = update['title']
                albums.author = update['author']
                albums.year = update['year']
        print ("The album is modified")