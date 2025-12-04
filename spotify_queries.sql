-- Analysis with spotify data 
use spotify_db;

Select * from spotify_tracks;

-- Top 5 tracks by popularity
SELECT track_name, artist, popularity
FROM spotify_tracks
ORDER BY Popularity DESC
LIMIT 5;


-- Longest vs shortest songs
SELECT track_name , artist, duration_minutes
FROM spotify_tracks
ORDER BY duration_minutes DESC;


-- Average popularity overall
SELECT AVG(Popularity) AS avg_popularity
FROM spotify_tracks;

-- Average popularity by artist
SELECT Artist, AVG(Popularity) AS avg_pop
FROM spotify_tracks
GROUP BY Artist
ORDER BY avg_pop DESC;


-- Categorise songs by duration (short, medium, long)
SELECT 
    track_name,
    Artist,
    duration_minutes,
    CASE
        WHEN duration_minutes < 3 THEN 'Short'
        WHEN duration_minutes BETWEEN 3 AND 4 THEN 'Medium'
        ELSE 'Long'
    END AS DurationCategory
FROM spotify_tracks;


-- Songs Per Artist
SELECT artist, COUNT(*) AS song_count
FROM spotify_tracks
GROUP BY artist
ORDER BY song_count DESC;

-- Most Popular Song 
SELECT track_name, popularity
FROM spotify_tracks
ORDER BY popularity DESC
LIMIT 1;


