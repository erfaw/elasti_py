import spotipy, os
# from spotipy.oauth2 import SpotifyClientCredentials
import subprocess; subprocess.call('cls', shell=True)

## CLASS DECLARATION
class SpotifyHandler(spotipy.client.Spotify):
    def __init__(self):
        """using 'Spotipy' library, handle works with spotify things. MAKE CLIENT SPOTIFY OBJECT TO WORK WITH SPOTIFY WEB API"""
        self.get_credentials_from_EV()
        self.make_auth_agent()
        super().__init__(auth_manager=self.auth_manager)

        self.playlists: dict = {}

    def get_credentials_from_EV(self):
        """TAKE CLIENT CREDENTIALS FROM EV AND STORE IT"""
        self.client_id = os.environ.get("SPOTIFY_CLIENT_ID_erfawn.h@gmail.com")
        self.client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET_erfawn.h@gmail.com")
        self.USER_NAME="3xvuew854p1lasq1qzugv5wlv"

    def make_auth_agent(self):
        """MAKE 'AUTH_MANAGER' OBJECT TO PASS CLIENT SPOTIFY CLASS""" 
        self.auth_manager = spotipy.oauth2.SpotifyOAuth(
            client_id= self.client_id,
            client_secret= self.client_secret,
            redirect_uri= "https://example.org/callback",
            scope= "playlist-modify-private",
            username= self.USER_NAME,
            cache_path= './Day046-erf/token.json'
        )
    
    def create_playlist(self, name, description='', ):
        """CREATE A PLAYLIST FOR USER"""
        playlist_created = self.user_playlist_create(
            user= self.USER_NAME,
            name= name,
            public=False,
            collaborative= False,
            description= description
        )
        new_playlist = {
            name: playlist_created['external_urls']['spotify']
        }
        self.playlists.update(new_playlist)


    def user_playlist(self):
        """PRINT PLAYLIST MADE BY AN 'ID_USER'""" 
        playlists = self.user_playlists(self.USER_NAME)
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                print(f"{i + 1 + playlists['offset']:4d} {playlist['uri']} {playlist['name']}")
            if playlists['next']:
                playlists = self.next(playlists)
            else:
                playlists = None
                break

    def all_albums_by(self, url):
        """PRINT ALL ALBUMS RELEASED BY 'ID_ARITST', need to insert url_address of that particular artist, or uri, or just id"""
        results = self.artist_albums(url, album_type='album')
        albums = results['items']
        while results['next']:
            results = self.next(results)
            albums.extend(results['items'])

        for album in albums:
            print(album['name'])
