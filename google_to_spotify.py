## Creating a program which takes songs from a google saved list or whatever and adding them to a created spotify playlist
#   https://developer.spotify.com/
#   https://developers.google.com/youtube/v3
#   https://github.com/ytdl-org/youtube-dl
#
import json
import requests
from secrets import spotify_user_id

class CreatePlaylist:

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token spotify_token

    # Log into Youtube 
    def get_youtube_client(self):
        pass

    # get the liked videos 
    def get_liked_videos(self):
        pass
    
    # Create a new playlist
    def create_playlist(self):

        req_body = json.dumps({
                   "name": "Youtube Liked Music",
                   "description": "Liked Youtube videos",
                   "public": True
        })

        query = "https://api.spotify.com/v1/users/{1188322136}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "content-Type":"applications/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # Playlist id
        return response_json["id"]

    # spearch for song
    def get_spotify_uri(self, song_name, artist):

        query = "https://api.spotify.com/v1/search?type=track%2Cartist&limit=10&offset=5".format(song_name,artist)


        response = requests.post(
            query,
            data=request_body,
            headers={
                "content-Type":"applications/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        
        response_json = response.json()
        songs = repsonse_json["tracks"]["items"]

        # only use the first song
        uri = songs[0]["uri"]

        return uri

    # add song to new spotify playlist
    def song_2_playlist(self):
        pass

if __name__ == "__main__":
        pass