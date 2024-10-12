from spotify import get_playlist_tracks, get_user_playlists
from youtube_music import create_playlist
# Example usage:
if __name__ == "__main__":
    # Step 1: Get the list of playlists
    playlists = get_user_playlists()

    # Ask the user to select a playlist by index
    selected_index = int(input("Enter the playlist number to fetch its songs: ")) - 1
    selected_playlist_id = playlists[selected_index][1]

    # Step 2: Get all songs in the selected playlist
    all_tracks = get_playlist_tracks(selected_playlist_id)

    # Step 3: Create playlist
    unavailable_songs =  create_playlist(all_tracks)

    if not unavailable_songs:
        print("All songs were added successfully")
    else:
        print(f"Was unable to find {unavailable_songs} songs")
