from bs4 import BeautifulSoup
import requests

def news(args:any = ''):
    url = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"

    res = requests.get(url)

    soup = BeautifulSoup(res.content , 'html.parser')
    data = soup.find_all('div' , {'jscontroller':'d0DtYd'})[:5]

    final_news_list = ''

    for ele in data:
        final_news_list+='\n\n'+ele.h3.text
        final_news_list+='\nRead More Here : https://news.google.com/'+ele.h3.find('a').get("href")[1:]
    
    return "The Top 3 News of the Day are :\n\n"+final_news_list


if __name__ == '__main__':
    print(news())
