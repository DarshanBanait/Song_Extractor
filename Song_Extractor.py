import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
client_id = 'Your spotify client_id'
client_secret = 'Your spotify client_secret'
redirect_uri = 'http://localhost:8888/callback'  # Set this as the redirect URI in your Spotify Developer application

# Initialize the Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='playlist-read-private'))

# Playlist ID of your "My Favorites" playlist
playlist_id = 'Your spotify playlist_id'

# Get the playlist
playlist = sp.playlist(playlist_id, fields='tracks')

# Extract and print the song names
song_names = [track['track']['name'] for track in playlist['tracks']['items']]

# Write the song names to a text file
with open('favorite_songs.txt', 'w', encoding='utf-8') as file:
    for song_name in song_names:
        file.write(song_name + '\n')

print('Song names extracted and saved to favorite_songs.txt')
