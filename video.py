#https://www.youtube.com/results?search_query=tree
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from messages import n # New Line or \n, in a whatsapp friendly format
from sender import sendMessage


def video(search=''):
    if isinstance(search, list):
        search_item = '+'.join(search)
        search = " ".join(search)
    elif search == '':
        search_item = "India"
        search = "India"
    else:
        search_item = search

    # search = search.replace(" ", "+")

    base_url = "https://www.youtube.com"
    query = f"/results?search_query={search_item}"

    soup = BeautifulSoup(
        requests.get(base_url + query).content,    # Web Page to Open
        'html.parser'           # Parser to use
    )
    results = soup.find_all('a',{'class':'yt-uix-sessionlink'}) # Get all contents from the Session Links

    resp = []
    vid_counter = 0
    sub = {
        1:'st',
        2:'nd',
        3:'rd',
        4:'th',
        5:'th',
        6:'th',
        7:'th',
        8:'th',
        9:'th',
        10:'th'
    }

    for link_no in range(0, len(results), 2):
        vid_link = results[link_no].get("href")
        if "watch" in vid_link:
            vid_counter+=1
            resp.append(f"The {int(vid_counter)}{sub[int(vid_counter)]} *most relevent* \nVideo reguarding --> {search} : "+ n + base_url + vid_link)
        
        if len(resp) == 3:
            break
    
    if len(resp) == 0:
        resp = "No Response From the Server, please Try Again.... "

    return resp


def download_video(search=""):
    youtubeLinks = video(search)

    dlLinks = []
    if isinstance(youtubeLinks, list):
        place = 63 + len(" ".join(search))
        for link in youtubeLinks:
            dlLinks.append(link[:place]+'ss'+link[place:])
    else:
        dlLinks = youtubeLinks
        
    return dlLinks


    
if __name__ == '__main__':
    # search = input("Enter what to Search : ")
    search = "Ped Paudha"
    search = search.split(' ')

    response = download_video(search=search)

    if isinstance(response,list):
        for video in response[:-1]:
            sendMessage(msg=video)
            print(video)
        
        response = response[-1]
    
    sendMessage(msg=response)
    # print(response)