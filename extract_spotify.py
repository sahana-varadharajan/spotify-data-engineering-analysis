import requests
import base64

def get_token(client_id, client_secret):
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    r = requests.post(url, headers=headers, data=data)
    token = r.json()["access_token"]
    return token



def extract_track(track_url, token):
    track_id = track_url.split("/")[-1].split("?")[0]
    api_url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(api_url, headers=headers)
    return res.json()

