import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

# Users date of choice to scrape
answer = input("What date would you like to travel to? Please enter the date as YYYY-MM-DD:")

URL = f"https://appbrewery.github.io/bakeboard-hot-100/{answer}/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Extracting song titles from website
song_titles = soup.find_all('h3', attrs={'class': 'chart-entry__title'})
# for song_title in song_titles:
#     print(song_title.text)

# Authenticating YT Music via browser, removed file from upload due to security purposes
yt = YTMusic("browser.json")
playlist_id = ""
video_id = ""

# Get current playlists to verify one for the specified date does not exist.
exists = False
current_playlists = yt.get_library_playlists()
if current_playlists:
    for playlist in current_playlists:
        if playlist["title"] == f"{answer} Billboard 100":
            print(f"{playlist["title"]} already exists!")
            playlist_id = playlist["playlistId"]
            exists = True
            break
# If the playlist does not exist, create it
if not exists:
    new_playlist = yt.create_playlist(title=f"{answer} Billboard 100", description=f"Playlist for {answer} Billboard 100")
    playlist_id = new_playlist["playlistId"]
    print(f"Playlist for {answer} Billboard 100 created.")

# Pass song titles to YT music and take the first result.
for song in song_titles:
    successful = True
    # noinspection broad-exception
    try:
        search_list = yt.search(query=song.text,filter="songs")
        video_id = search_list[0]["videoId"]
    except Exception:
        successful = False
        print("Failed")
        pass
# If successfully searched, add first result to playlist
    if successful:
        yt.add_playlist_items(playlistId=playlist_id, videoIds=[video_id])
        print(f"Added {song.text} to {answer} Billboard 100")



