# Spotify Data Engineering & Analysis

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![Status](https://img.shields.io/badge/Status-Active-green)

A mini-intermediate data engineering and analytics project that pulls Spotify playlist data, stores it in MySQL, and allows for analysis using Python.

---

## Overview
This project started as a simple “I want to explore my playlists” idea 🎧 and grew into a small, reusable pipeline. It demonstrates practical skills in data extraction, storage, and analysis, with room for future enhancements like dashboards 📊 and ETL pipelines 🔄.

---

## What This Project Does
- Reads playlist URLs from a text file
- Fetches track details using the Spotify API
- Loads tracks into a MySQL database
- Exports a clean CSV for analysis
- Includes Python scripts for further analysis and experimentation

---

## Tech Stack
🐍 Python

🎵 Spotipy (Spotify Web API wrapper)

💾 SQLAlchemy + MySQL

📊 Pandas / Matplotlib 

---

## Project Structure
```
project/
├── data/          📂 Exported CSVs
├── notebooks/     📓 Experiments and EDA
├── scripts/       🛠️ Core Python scripts (ETL, export, etc.)
├── sql/           💾 SQL table setup
├── requirements.txt 📦 Python dependencies
└── README.md      📝 Project overview and instructions
 ```


---

## Database
Tracks are stored in a MySQL table with this structure:
- track_name
- artist
- album
- popularity
- duration_minutes

---

## Setup
1. Install dependencies:
   ``` pip install -r requirements.txt ```

2. Set up MySQL:
   Open spotify_mysql.ipynb in Jupyter Notebook 🖥️.
   Run all cells to create the MySQL table.

3. Add playlist URLs:
   Edit track_url.txt 📄 (or playlist_urls.txt) with Spotify track/playlist links, one per line.

4 . Fetch and store data:
    Open spotify_sql_urls.ipynb in Jupyter Notebook and run all cells. This will fetch track info from Spotify and insert it into MySQL.
    Also visualization and taking snapshot of the table for reference.

5. Export the final CSV:
   ``` python scripts/export_csv.py  ```
   The CSV will be generated in data/spotify_export.csv 📂

---

## .gitignore

Exclude sensitive or unnecessary files:

.env (credentials)

.cache

data/exported_csvs (optional)

.ipynb_checkpoints


---
## Future Enhancements

Schedule ETL with Airflow 

Build an interactive Streamlit dashboard

Add more Spotify audio features (tempo, key, mood)

Playlist comparisons and clustering

---

## Credits

Inspired by Gowtham’s tutorial (https://www.youtube.com/watch?v=gJUJ1yFHlwU&list=PLLa_h7BriLH3LrJ45gDKIoyqpcuXgzxLL&index=15). I extended this project by building an ETL pipeline, adding custom track analysis, and structuring it for reuse.














