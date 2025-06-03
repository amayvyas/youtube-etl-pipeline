import pandas as pd
import streamlit as st

# Load cleaned CSV (avoid DB connection issues on Streamlit Cloud)
df = pd.read_csv("data/cleaned_videos.csv")

st.set_page_config(page_title="YouTube Channel Analytics", layout="wide")

st.title("📊 YouTube Channel Video Analytics")

# Show basic stats
st.metric("Total Videos", len(df))
st.metric("Earliest Upload", df["published_at"].min())
st.metric("Latest Upload", df["published_at"].max())

# Convert published_at to datetime for plotting
df["published_at"] = pd.to_datetime(df["published_at"])

# Line chart of uploads over time
st.subheader("Video Upload Trend Over Time")
df_by_month = df.groupby(df["published_at"].dt.to_period("M")).size().rename("Uploads").reset_index()
df_by_month["published_at"] = df_by_month["published_at"].astype(str)
st.line_chart(df_by_month.set_index("published_at"))

# Search/filter
st.subheader("Search Videos")
search_term = st.text_input("Enter keyword:")
if search_term:
    filtered = df[df["title"].str.contains(search_term, case=False)]
    st.write(filtered)
else:
    st.write(df)
