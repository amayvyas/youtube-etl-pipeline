import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("YT_API_KEY")
CHANNEL_ID = os.getenv('CHANNEL_ID')

BASE_URL = "https://www.googleapis.com/youtube/v3"

# Load data
def get_uploads_playlist_id(channel_id):
    url = f"{BASE_URL}/channels?part=contentDetails&id={channel_id}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if "items" not in data or not data["items"]:
        raise Exception(f"Invalid response for channel ID {channel_id}: {data}")
    
    return data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

def get_videos_from_playlist(playlist_id, max_results=20):
    url = f"{BASE_URL}/playlistItems?part=snippet&playlistId={playlist_id}&maxResults={max_results}&key={API_KEY}"
    response = requests.get(url)
    return response.json()

# Save raw data into json
def save_raw_data(data):
    with open("data/raw_data.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    uploads_playlist = get_uploads_playlist_id(CHANNEL_ID)
    video_data = get_videos_from_playlist(uploads_playlist)
    save_raw_data(video_data)
    print("✅ Data pulled and saved to data/raw_data.json")