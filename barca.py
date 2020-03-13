# This Web Scraping script performs the following tasks:
# (1) Scrape two renowned football websites, viz. Marca and Barca Blaugranes for FC Barcelona news
# (2) Find today's news articles and open them in new tabs in Google Chrome

import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import webbrowser

def main():
    cur_date = str(datetime.date(datetime.now()))   # Find current date
    date = datetime.today() # Find current date
    year, month, day = str(date.year), str(date.month), str(date.day)
    trim_date = year + month + day
    url_marca = 'https://www.marca.com/en/football/barcelona.html?intcmp=MENUPROD&s_kw=english-barcelona'
    url_sbnation = 'https://www.barcablaugranes.com/archives/' + year + '/' + month
    response_marca, response_sbnation = requests.get(url_marca), requests.get(url_sbnation)
    src_marca, src_sbnation = response_marca.text, response_sbnation.text
    soup_marca, soup_sbnation = bs(src_marca, 'lxml'), bs(src_sbnation, 'lxml')

    # Store all the news cards from the current first page of Marca in a list
    cards_marca = soup_marca.find_all('li', class_ = 'content-item')

    # Store all the news cards from the current first page of Barca Blaugranes in a list
    cards_sbnation = soup_sbnation.find_all('div', class_ = 'c-compact-river__entry')

    try:
        for card in cards_marca:
            link = card.h3.a['href']
            check = link.split('/')
            date = '-'.join(check[-4:-1])   # Check if the article's date matches the current date
            if date == cur_date:
                webbrowser.open(link)
    except Exception as e:
        pass
    try:
        for card in cards_sbnation:
            link = card.h2.a['href']
            check = link.split('/')
            if trim_date == ''.join(check[-5:-2]):  # Check if the article's date matches the current date
                webbrowser.open(link)
    except Exception as e:
        pass

if __name__ == '__main__':
    main()
