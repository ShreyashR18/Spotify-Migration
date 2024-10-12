from ytmusicapi import YTMusic
from tqdm import tqdm 

#Create an instance of YTMusic using the oath.json file
ytmusic = YTMusic("oauth.json")

#Create a playlist with the songs provided from Spotify Playlist
def create_playlist(song_list):
    #Creates a blank playlist
    playlistId = ytmusic.create_playlist("Spotify playlist New", "Created using the API")
    unavailable_songs = 0
    for song in tqdm(song_list, desc="Adding songs to playlist", unit="song"):
        search_results = ytmusic.search(song)
        if search_results:
            status = ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
        else:
            unavailable_songs += 1
    #Returns numbers of songs it was unable to find
    return unavailable_songs