import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Read environment variables
DB_HOST = os.getenv("PG_HOST")
DB_PORT = os.getenv("PG_PORT")
DB_NAME = os.getenv("PG_DATABASE")
DB_USER = os.getenv("PG_USER")
DB_PASSWORD = os.getenv("PG_PASSWORD")

# Read cleaned data
df = pd.read_csv("data/cleaned_videos.csv")

conn = None
cursor = None

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    print("✅ Connected to PostgreSQL")

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO youtube_videos (video_id, title, published_at)
            VALUES (%s, %s, %s)
            ON CONFLICT (video_id) DO NOTHING;
        """, (row["video_id"], row["title"], row["published_at"]))

    conn.commit()
    print(f"✅ Loaded {len(df)} rows into the database.")

except Exception as e:
    print("❌ Error:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
