import mysql.connector

def load_to_mysql(data):
    conn = mysql.connector.connect(host="localhost", user="root", password="your_password", database="spotify_db")
    cur = conn.cursor()

    insert = """
    INSERT INTO spotify_tracks(`track_name`, `artist`, `album`, `popularity`, `duration_minutes`)
    VALUES (%s, %s, %s, %s, %s)
    """

    for row in data:
        cur.execute(insert, list(row.values()))
    
    conn.commit()
    conn.close()
