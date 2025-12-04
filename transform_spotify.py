def clean_track(track):
    return {
        "Track Name": track["name"],
        "Artist": track["artists"][0]["name"],
        "Album": track["album"]["name"],
        "Popularity": track["popularity"],
        "Duration (minutes)": track["duration_ms"] / 60000
    }