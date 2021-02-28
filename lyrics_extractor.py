import requests
from bs4 import BeautifulSoup

google_base_url = "https://www.google.com/search?q=lyrics%20"

def get_lyrics(song_name):
    query  = song_name.replace(' ', '%20')

    page = requests.get(url=google_base_url + query)
    soup = BeautifulSoup(page.content, 'lxml')

    lyrics = soup.select('.tAd8D')

    strLyrics = []

    paras = list(lyrics)

    title  = paras[0].getText()
    lyrics = paras[3].getText()

    return title, lyrics