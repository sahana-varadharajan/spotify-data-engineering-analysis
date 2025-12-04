# export_csv.py
import os
import pandas as pd
from sqlalchemy import create_engine

def export_csv():
    print("Export function started...")

    data_folder = os.path.join(os.getcwd(), "data")
    os.makedirs(data_folder, exist_ok=True)

    # SQLAlchemy engine for MySQL
    engine = create_engine("mysql+pymysql://root:yourpassword@localhost/spotify_db")

    try:
        # Read the table into pandas
        df = pd.read_sql("SELECT * FROM spotify_tracks", engine)
        print("DataFrame loaded successfully!")
        print(df.head())  # Print first 5 rows as a snapshot
    except Exception as e:
        print("Error loading DataFrame:", e)
        return

    # Save CSV into the 'data' folder
    csv_path = os.path.join(data_folder, "spotify_export.csv")
    df.to_csv(csv_path, index=False)
    print(f"CSV export complete! File saved at: {csv_path}")

if __name__ == "__main__":
    export_csv()
