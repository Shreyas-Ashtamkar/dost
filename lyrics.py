from lyrics_extractor import get_lyrics

def getLyrics(song_title=""):
    if isinstance(song_title, list):            # Check if input is a list of Words
        song_title = " ".join(song_title)       
    elif song_title == '':                      # Check of input is blank
        song_title = "Vande Mataram"
    
    song_head, song_lyrics = get_lyrics(song_title)

    if song_head !='' and song_lyrics != '':
        response = f"Lyrics for {song_head} is as follows : \n\n{song_lyrics}"
        response = response.split('\n\n')

    else:
        response ="Err: No lyrics found for " + song_title
    
    return response

if __name__ == "__main__":
    from sender import sendMessage

    song_title = "Hundred Miles"
    song_title = song_title.split()

    msg = getLyrics(song_title)

    if isinstance(msg, list):
        msg = "\n\n".join(msg)        
        

    msg += "\n\nType help for more options."
    
    sendMessage(msg=msg)
