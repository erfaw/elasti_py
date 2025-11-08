from spotify_handler import SpotifyHandler
from songs_details import SongsData
from pathlib import Path
_file_dir = Path(__file__).resolve().parent

spotify = SpotifyHandler()
songs = SongsData()

## catch songs list in given date
songs.web_page = songs.get_html_at(input("Which year do you want to travel to? (Type the date in this format YYYYMMDD)\n\t"))
songs.scrapte_to_songs_list()
print(songs.songs_db)
songs.store_to_excel(_file_dir)


