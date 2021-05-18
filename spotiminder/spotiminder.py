"""Main module."""
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from jsonschema import validate
import time
import threading
import os
import base64

# Prefixes for Spotify URIs
playlist_prefix = "spotify:playlist:"

# Request all scopes that allow us to update playlist metadata.
scope = "ugc-image-upload,playlist-modify-public,playlist-modify-private"

# Our playlist metadata JSON schema definition.
schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "description": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name",
        "description"
      ]
    }
  ]
}

"""Verify that the playlist metadata is in the right format."""
def load_json(path):
    with open(path, "r") as json_file:
        data = json.load(json_file)
        validate(instance=data, schema=schema)
        return data

"""Update the specified playlist's cover image, if it exists."""
def update_playlist_image(id, name):
    global image_folder
    filename = os.path.join(image_folder, id + ".jpg")
    with open(filename, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read())
        sp.playlist_upload_cover_image(id, base64_string)
        print("Updated cover image for '" + name + "'")

"""Update the specified playlist's metadata."""
def update_playlist(id, name, description):
    sp.playlist_change_details(id, name=name, description=description)
    print("Updated name and description for '" + name + "'")

    # If the user provided an image folder, try that now.
    global image_folder
    if image_folder != "":
        update_playlist_image(id, name)

"""Check the specified playlist's name and description against our metadata.

If it doesn't match, go update all metadata.
"""
def check_playlist(id, name, description):
    result = sp.playlist(playlist_prefix + id, fields='name,description')

    if result["name"] != name or result["description"] != description:
        update_playlist(id, name, description)

"""Check the next playlist's metadata."""
def check_next_playlist():
    global playlists
    global currentIndex
    playlist = playlists[currentIndex]
    check_playlist(playlist["id"], playlist["name"], playlist["description"])

    # Move to the next playlist or set the timer.
    currentIndex += 1
    if currentIndex < len(playlists):
        check_next_playlist()
    else:
        global interval
        timer = threading.Timer(interval, check_playlists)
        timer.start()

"""Start the process of checking all playlists."""
def check_playlists():
    # Reset global state before we begin processing.
    global currentIndex
    currentIndex = 0

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time + ": Checking playlists.")
    check_next_playlist()

"""Entry-point for the module."""
def main(args):
    # Authenticate the user. This may already be cached.
    global sp
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=args.client_id,
                                                   client_secret=args.client_secret,
                                                   redirect_uri=args.redirect_uri,
                                                   scope=scope))

    # Validate the playlist metadata file.
    global playlists
    playlists = load_json(args.json_file)

    # Set global state before processing.
    global interval
    interval = args.interval
    global image_folder
    image_folder = args.image_folder

    print("Exit with Ctrl+C")

    # Start our main processing loop.
    check_playlists()


