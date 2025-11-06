## IMPORTS
import spotipy, os
from spotipy.oauth2 import SpotifyClientCredentials
import subprocess as sp; sp.call('cls', shell=True)

## TAKE CLIENT CREDENTIALS FROM EV
spotify_client_id = os.environ.get("SPOTIFY_CLIENT_ID_erfawn.h@gmail.com")
spotify_client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET_erfawn.h@gmail.com")

## MAKE 'AUTH_MANAGER' OBJECT TO PASS CLIENT SPOTIFY CLASS
USER_NAME="3xvuew854p1lasq1qzugv5wlv"
auth_manager = spotipy.oauth2.SpotifyOAuth(
    client_id= spotify_client_id,
    client_secret= spotify_client_secret,
    redirect_uri= "https://example.org/callback",
    scope= "playlist-modify-private",
    username= USER_NAME,
    cache_path= './Day046-erf/token.json'
)
## MAKE CLIENT SPOTIFY OBJECT TO WORK WITH SPOTIFY WEB API
sp1 = spotipy.client.Spotify(auth_manager=auth_manager)

## CREATE A PLAYLIST FOR USER
playlist_created = sp1.user_playlist_create(
    user= USER_NAME,
    name= "A testing Playlist <3 !!",
    public=False,
    collaborative= False,
    description= "just testing"
)
print(playlist_created)



## PRINT PLAYLIST MADE BY AN 'ID_USER' 
        # playlists = sp.user_playlists('3xvuew854p1lasq1qzugv5wlv')
        # print(playlists)
        # while playlists:
        #     for i, playlist in enumerate(playlists['items']):
        #         print(f"{i + 1 + playlists['offset']:4d} {playlist['uri']} {playlist['name']}")
        #     if playlists['next']:
        #         playlists = sp.next(playlists)
        #     else:
        #         playlists = None

## PRINT ALL ALBUMS RELEASED BY 'ID_ARITST'
        # erfan_paydar_url = "https://open.spotify.com/artist/1yPzb9mqugowOfUs2vIOgL"
        # results = sp.artist_albums(erfan_paydar_url, album_type='album')
        # albums = results['items']
        # while results['next']:
        #     results = sp.next(results)
        #     albums.extend(results['items'])

        # for album in albums:
        #     print(album['name'])
