import streamlit as st
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# DB connection info
DB_HOST = os.getenv("PG_HOST")
DB_PORT = os.getenv("PG_PORT")
DB_NAME = os.getenv("PG_DATABASE")
DB_USER = os.getenv("PG_USER")
DB_PASSWORD = os.getenv("PG_PASSWORD")

# Connect to DB
@st.cache_data
def fetch_data():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    query = "SELECT video_id, title, published_at FROM youtube_videos ORDER BY published_at DESC"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Load data
st.title("📺 YouTube Channel Video Dashboard")

try:
    df = fetch_data()
    df["published_at"] = pd.to_datetime(df["published_at"])

    # Show metrics
    st.metric("Total Videos", len(df))

    # Filter
    search = st.text_input("🔍 Search video titles")
    if search:
        df = df[df["title"].str.contains(search, case=False)]

    # Bar chart: videos by month
    df["month"] = df["published_at"].dt.to_period("M").astype(str)
    monthly_count = df.groupby("month").size().reset_index(name="video_count")
    st.subheader("📊 Videos Uploaded per Month")
    st.bar_chart(monthly_count.set_index("month"))

    # Latest videos
    st.subheader("🆕 Latest Videos")
    st.dataframe(df[["title", "published_at"]].head(10), use_container_width=True)

except Exception as e:
    st.error(f"Error fetching data: {e}")
