from spotify_handler import SpotifyHandler
from songs_details import SongsData
from pathlib import Path
_file_dir = Path(__file__).resolve().parent

spotify = SpotifyHandler()
songs = SongsData()

## CATCH SONGS HTML IN GIVEN DATE AND SCRAPE AND MAKE DATAFRAME
songs.web_page = songs.get_html_at(input("Which year do you want to travel to? (Type the date in this format YYYYMMDD)\n\t"))
songs.scrapte_to_songs_list()

## BUILD NEW COLUMN IN DATAFRAME FOR URLS
songs.songs_db.insert(len(songs.songs_db.columns), "URL/URI/ID", value={}, allow_duplicates=False)
## collect and add to column
for song in songs.songs_db.iterrows():
    search_result = spotify.search(
        q= f"{song[1].Artist} - {song[1].Title}",
        limit= 1
    )
    # if song[1].Title == search_resutl['tracks']['items'][0]['name']:
    song_url = search_result['tracks']['items'][0]['external_urls']['spotify']
    songs.songs_db.loc[songs.songs_db['Title'] == song[1].Title, "URL/URI/ID"] = song_url

songs.store_to_excel(_file_dir)


