# YouTube ETL Pipeline & Analytics Dashboard

This repository contains a complete end-to-end data engineering project that extracts YouTube video metadata, transforms the data, loads it into a PostgreSQL database, and visualizes key insights using a Streamlit dashboard.

---

## 🚀 Project Overview

- **Extract** YouTube video metadata using YouTube API.
- **Transform** the raw data with pandas (cleaning, filtering, formatting).
- **Load** the cleaned data into a PostgreSQL database.
- **Visualize** the video analytics with an interactive Streamlit dashboard.

This project demonstrates a real-world data engineering workflow — from data ingestion to live dashboarding.

---

## 📊 Live Demo

Check out the live Streamlit dashboard here:  
https://youtube-etl-pipeline-dzu7irzweoxjbubug2fbtu.streamlit.app

---

## 🛠️ Tech Stack

- Python
- YouTube Data API v3
- pandas
- PostgreSQL
- psycopg2
- Streamlit
- dotenv for environment management

---

## 📝 Setup & Run Locally

### 1. Clone the repo:
   ```bash
   git clone https://github.com/amayvyas/youtube-etl-pipeline.git
   cd youtube-etl-pipeline
   ```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your .env
### Create a .env file in the root with your PostgreSQL credentials:

```bash
PG_HOST=your_host
PG_PORT=5432
PG_DATABASE=your_db
PG_USER=your_user
PG_PASSWORD=your_pass
```

### 4. Run the ETL pipeline

```bash
python ingest.py
python transform.py
python load.py
```

### 5. Run the Streamlit dashboard:

```bash
streamlit run yt-data-pipeline/dashboard.py
```

### 📂 Project Structure

``` 
youtube-etl-pipeline/
├── data/
│   └── cleaned_videos.csv        # Cleaned data used for loading & dashboard
├── yt-data-pipeline/
│   ├── ingest.py                 # Extract data from YouTube API
│   ├── transform.py              # Transform and clean the raw data
│   ├── load.py                   # Load data into PostgreSQL
│   └── dashboard.py              # Streamlit dashboard for visualization
├── .env.example                  # Example environment variables
├── requirements.txt
└── README.md
```

### 🛡️ Notes
 - The dashboard reads from data/cleaned_videos.csv to avoid database dependency during demo.

 - Make sure to push cleaned_videos.csv to GitHub or the app will fail to load the data.

 - For production, connect the dashboard to PostgreSQL for real-time analytics.

### 📜 License
MIT License

### 🤝 Contributions & Feedback
PRs, issues, and suggestions are welcome!
This is a personal portfolio project aiming to showcase a data engineering workflow end-to-end.

### 📞 Contact
> Amay Vyas – amay22vyas@gmail.com <br>
> GitHub: https://github.com/amayvyas
