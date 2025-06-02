# 📺 YouTube Data Engineering Pipeline

This project is a full-fledged **ETL pipeline** that fetches video metadata from the **YouTube Data API**, transforms it using **pandas**, loads it into a **PostgreSQL database**, and visualizes key metrics with a **Streamlit dashboard**.

> 💼 Built to showcase real-world data engineering skills — ingestion, transformation, storage, and analytics — all modular and production-ready.

---

## 🚀 Tech Stack

| Layer         | Tools Used                     |
|---------------|--------------------------------|
| Ingestion     | YouTube Data API, `requests`   |
| Transformation| `pandas`                       |
| Storage       | `PostgreSQL`, `psycopg2`       |
| Dashboard     | `Streamlit`                    |
| Config Mgmt   | `.env`, `python-dotenv`        |

---

## 🧱 Architecture

+-------------+ +----------------+ +------------------+ +-----------------+
| YouTube API | --> | ingest.py | --> | transform.py | --> | load.py |
+-------------+ +----------------+ +------------------+ 

| PostgreSQL DB |
+--------+--------+
|
v
+-----------------+
| Streamlit Dash |
| dashboard.py |
+-----------------+


## 🧪 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/yt-data-pipeline.git
cd yt-data-pipeline
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

### 📌 Features
 - Pulls real data using YouTube Data API

 - Cleans and transforms with pandas

 - Inserts safely with PostgreSQL and ON CONFLICT

 - Filter/search in the dashboard

 - Production-ready with environment isolation


### 📜 License
MIT License

### 🙌 Contributing
Feel free to fork, raise issues or PRs. This project is built for learning and showcasing, so extend it however you want!