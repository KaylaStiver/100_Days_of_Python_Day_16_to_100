import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

movie_titles = soup.find_all('a', attrs={'data-test': True})
movie_titles = movie_titles[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    count = 1
    for movie in movie_titles:
        text = movie.text
        while text != "":
            text = text.replace("\n", " ")
            if "," in text:
                movie_title = text.split(",",1)[0]
                real_title = "The " + movie_title
                file.write(f"{count}{') '}{real_title}\n")
                count += 1
                break
            else:
                file.write(f"{count}{') '}{text}\n")
                count += 1
                break

