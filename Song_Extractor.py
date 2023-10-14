import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
client_id = '63ead25c6796405385f2f8be8b937691'
client_secret = '7d51fb1ec8b54081ada1f9e33348d628'
redirect_uri = 'http://localhost:8888/callback'  # Set this as the redirect URI in your Spotify Developer application

# Initialize the Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='playlist-read-private'))

# Playlist ID of your "My Favorites" playlist
playlist_id = '4LlehsGOThOGhW2mLQTYZd'
# https://open.spotify.com/playlist/4LlehsGOThOGhW2mLQTYZd?si=a8904e8657d4451b

# Get the playlist
playlist = sp.playlist(playlist_id, fields='tracks')

# Extract and print the song names
song_names = [track['track']['name'] for track in playlist['tracks']['items']]

# Write the song names to a text file
with open('favorite_songs.txt', 'w', encoding='utf-8') as file:
    for song_name in song_names:
        file.write(song_name + '\n')

print('Song names extracted and saved to favorite_songs.txt')
