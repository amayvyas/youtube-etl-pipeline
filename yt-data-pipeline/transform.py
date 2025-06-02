import json
import pandas as pd

with open("data/raw_data.json") as f:
    raw_data = json.load(f)

videos = raw_data['items']

rows = []

for item in videos:
    snippet = item['snippet']
    rows.append({
        "video_id":snippet['resourceId']['videoId'],
        "title":snippet['title'],
        "published_at":snippet['publishedAt']
    })

df = pd.DataFrame(rows)
df['published_at'] = pd.to_datetime(df['published_at'])

df.to_csv("data/cleaned_videos.csv", index=False)
print("✅ Cleaned data saved to data/cleaned_videos.csv")
