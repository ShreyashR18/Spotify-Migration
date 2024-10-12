import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Your Spotify API credentials
client_id = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
client_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
redirect_uri = 'http://localhost:8888/callback'  # Redirect URI from Spotify Dashboard

# Scope to read user's playlists and playlist tracks
scope = "playlist-read-private"

# Authenticate and handle user login
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Step 1: Get the user's playlists
def get_user_playlists():
    playlists = sp.current_user_playlists(limit=50)  # Fetch first 50 playlists
    playlist_info = []
    
    for idx, item in enumerate(playlists['items']):
        print(f"{idx + 1}. {item['name']} - {item['id']}")
        playlist_info.append((item['name'], item['id']))
    
    return playlist_info

# Step 2: Get all the songs in a specific playlist by its ID
def get_playlist_tracks(playlist_id):
    tracks = []
    results = sp.playlist_tracks(playlist_id, limit=100)  # Fetch the first 100 tracks

    while results:
        for item in results['items']:
            track = item['track']
            tracks.append(f"{track['name']} by {track['artists'][0]['name']}")
        
        # Check if there's a next page of tracks
        results = sp.next(results) if results['next'] else None

    return tracks


