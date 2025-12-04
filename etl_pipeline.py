from extract_spotify import get_token, extract_track
from transform_spotify import clean_track
from load_spotify import load_to_mysql

CLIENT_ID = "your_spotify_client_id"
CLIENT_SECRET = "your_spotify_client_secret"

def run_pipeline(txt_file_path):
    token = get_token(CLIENT_ID, CLIENT_SECRET)
    rows = []

    with open(txt_file_path, "r") as f:
        urls = f.read().splitlines()

    for url in urls:
        raw = extract_track(url, token)
        cleaned = clean_track(raw)
        rows.append(cleaned)

    load_to_mysql(rows)

if __name__ == "__main__":
    run_pipeline("test_url.txt")
