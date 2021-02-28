import requests
from bs4 import BeautifulSoup

class Song_Lyrics():
    """
        Initialises a class Song_lyrics.
        It takes in Google Custom Search API & Google Engine ID as arguments.
        The ID and API key is used whenever get_lyrics function is called to fetch lyrics.
    """

    def __init__(self, GCS_API_KEY, GCS_ENGINE_ID):
        self.GCS_API_KEY = GCS_API_KEY
        self.GCS_ENGINE_ID = GCS_ENGINE_ID


    def get_lyrics(self, song_name):
        """
            Searches lyrics for the song name passed in.
            Autocorrects any song name spelling errors.
            Fetches and stores the HTML of received URL.
            Extracts Title & Lyrics from the HTML.
            Returns title and lyrics.
        """

        url = "https://www.googleapis.com/customsearch/v1/siterestrict?key=" + self.GCS_API_KEY + "&cx=" + self.GCS_ENGINE_ID + "&q=" + song_name.replace(" ","%20") + "%20lyrics"

        page = requests.get(url)
        data = page.json()

        try:
            # Gets URL of the first Result
            get_data = data["items"][0]["link"]
            # print(get_data)
            title = data["items"][0]["title"]
            # print(title)

            # getting the url of the site
            page = requests.get(get_data)
            soup = BeautifulSoup(page.content, 'lxml')

            # Method 1 Genius
            if 'genius' in get_data:

                extract = soup.findAll('div',class_="Lyrics__Container-sc-1ynbvzw-2")
                extracted = []

                for elem in extract:
                    for br in elem.findAll('br'):
                        br.replace_with("\n")
                    elem = elem.get_text().strip()
                    if elem != '':
                        extracted.append(elem)

                lyrics = "\n\n".join(extracted)
                title = title[:-16]

                # print("From inside : ",lyrics)


            # Method 2 Glamsham
            elif 'glamsham' in get_data:
                extract = soup.find_all('font', class_='general')[5]
                for br in extract.find_all("br"):   # This Prints out newlines instead of <br> tags
                    br.replace_with("\n")
                lyrics = extract.get_text()
                title = title[:-14].strip()

            # Method 3 LyricsBell
            elif 'lyricsbell' in get_data:
                extract = soup.select(".lyrics-col p")
                lyrics = ''
                for i in range(len(extract)):
                    lyrics += extract[i].get_text() + '<br><br>'
                title = title[:-13]

            # Method 4 LyricsTed
            elif 'lyricsted' in get_data:
                extract = soup.select(".lyric-content p")
                lyrics = ''

                for i in range(len(extract)):
                    # This Prints out newlines instead of <br> tags
                    lyrics += extract[i].get_text().strip() + '<br><br>'
                title = title

            # Method 5 LyricsOff
            elif 'lyricsoff' in get_data:
                extract = soup.select("#main_lyrics p")
                lyrics = ''

                for i in range(len(extract)):
                    # This Prints out newlines instead of <br> tags
                    lyrics += extract[i].get_text(separator="\n").strip() + '<br><br>'
                title = title
                
            # Method 6 LyricsMint
            elif 'lyricsmint' in get_data:
                extract = soup.select("#lyrics p")
                lyrics = ''

                for i in range(len(extract)):
                    # This Prints out newlines instead of <br> tags
                    lyrics += extract[i].get_text(separator="\n").strip() + '<br><br>'
                title = title
                # print("From inside",lyrics)
                lyrics = lyrics.replace('\n\n','\n')
            lyrics = lyrics.replace('<br>','\n')
            
        except Exception as e:
            print("Exception Occured : ", e)
            title = "Err: No lyrics found for " + song_name
            lyrics = ''
        
        # print(lyrics)

        return title, lyrics
