import requests
from bs4 import BeautifulSoup

answer = input("What date would you like to travel to? Please enter the date as YYYY-MM-DD:")

URL = "https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

song_titles = soup.find_all('h3', attrs={'class': 'chart-entry__title'})
for song_title in song_titles:
    print(song_title.text)

# header = {"User-Agent": "Mozilla/5.0 "
#                         "(Windows NT 10.0; Win64; x64; rv:155.0) "
#                         "Gecko/20100101 Firefox/155.0"}