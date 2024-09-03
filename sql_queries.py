# DROP TABLES

songplay_table_drop = """
IF EXISTS (SELECT name FROM sys.tables WHERE name='songplays')
BEGIN
    DROP TABLE songplays;
END
"""

user_table_drop = """
IF EXISTS (SELECT name FROM sys.tables WHERE name='users')
BEGIN
    DROP TABLE users;
END
"""

song_table_drop = """
IF EXISTS (SELECT name FROM sys.tables WHERE name='songs')
BEGIN
    DROP TABLE songs;
END
"""

artist_table_drop = """
IF EXISTS (SELECT name FROM sys.tables WHERE name='artists')
BEGIN
    DROP TABLE artists;
END
"""

time_table_drop = """
IF EXISTS (SELECT name FROM sys.tables WHERE name='time')
BEGIN
    DROP TABLE time;
END
"""

# CREATE TABLES

songplay_table_create = """
IF NOT EXISTS (SELECT name FROM sys.tables WHERE name='songplays')
BEGIN
    CREATE TABLE songplays (
        songplay_id INT IDENTITY(1,1) PRIMARY KEY,
        start_time DATETIME NOT NULL,
        user_id INT NOT NULL,
        level VARCHAR(255),
        artist_id VARCHAR(255),
        session_id INT,
        song_id VARCHAR(255),
        location VARCHAR(255),
        user_agent VARCHAR(255),
        CONSTRAINT FK_songplays_users FOREIGN KEY(user_id)
            REFERENCES users(user_id),
        CONSTRAINT FK_songplays_time FOREIGN KEY(start_time)
            REFERENCES time(start_time),
        CONSTRAINT FK_songplays_artists FOREIGN KEY(artist_id)
            REFERENCES artists(artist_id),
        CONSTRAINT FK_songplays_songs FOREIGN KEY(song_id)
            REFERENCES songs(song_id)
    );
END
"""

user_table_create = """
IF NOT EXISTS (SELECT name FROM sys.tables WHERE name='users')
BEGIN
    CREATE TABLE users (
        user_id INT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        gender VARCHAR(50),
        level VARCHAR(50)
    );
END
"""

song_table_create = """
IF NOT EXISTS (SELECT name FROM sys.tables WHERE name='songs')
BEGIN
    CREATE TABLE songs (
        song_id VARCHAR(255) PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        artist_id VARCHAR(255),
        year INT NOT NULL,
        duration FLOAT NOT NULL
    );
END
"""

artist_table_create = """
IF NOT EXISTS (SELECT name FROM sys.tables WHERE name='artists')
BEGIN
    CREATE TABLE artists (
        artist_id VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        location VARCHAR(255),
        latitude FLOAT,
        longitude FLOAT
    );
END
"""

time_table_create = """
IF NOT EXISTS (SELECT name FROM sys.tables WHERE name='time')
BEGIN
    CREATE TABLE time (
        start_time DATETIME PRIMARY KEY,
        hour INT,
        day INT,
        week INT,
        month INT,
        year INT,
        weekday INT
    );
END
"""

# INSERT RECORDS

songplay_table_insert = """
INSERT INTO songplays (
    start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
"""

# Insert for users table with update on conflict
user_table_insert = """
MERGE INTO users AS target
USING (SELECT ? AS user_id, ? AS first_name, ? AS last_name, ? AS gender, ? AS level) AS source
ON target.user_id = source.user_id
WHEN MATCHED THEN
    UPDATE SET first_name = source.first_name,
               last_name = source.last_name,
               gender = source.gender,
               level = source.level
WHEN NOT MATCHED THEN
    INSERT (user_id, first_name, last_name, gender, level)
    VALUES (source.user_id, source.first_name, source.last_name, source.gender, source.level);
"""

# Insert for songs table
song_table_insert = """
MERGE INTO songs AS target
USING (SELECT ? AS song_id, ? AS title, ? AS artist_id, ? AS year, ? AS duration) AS source
ON target.song_id = source.song_id
WHEN NOT MATCHED THEN
    INSERT (song_id, title, artist_id, year, duration)
    VALUES (source.song_id, source.title, source.artist_id, source.year, source.duration);
"""

# Insert for artists table
artist_table_insert = """
MERGE INTO artists AS target
USING (SELECT ? AS artist_id, ? AS artist_name, ? AS artist_location, ? AS artist_latitude, ? AS artist_longitude) AS source
ON target.artist_id = source.artist_id
WHEN NOT MATCHED THEN
    INSERT (artist_id, name, location, latitude, longitude)
    VALUES (source.artist_id, source.artist_name, source.artist_location, source.artist_latitude, source.artist_longitude);
"""

# Insert for time table
time_table_insert = """
MERGE INTO time AS target
USING (SELECT ? AS start_time, ? AS hour, ? AS day, ? AS week, ? AS month, ? AS year, ? AS weekday) AS source
ON target.start_time = source.start_time
WHEN MATCHED THEN
    UPDATE SET hour = source.hour,
               day = source.day,
               week = source.week,
               month = source.month,
               year = source.year,
               weekday = source.weekday
WHEN NOT MATCHED THEN
    INSERT (start_time, hour, day, week, month, year, weekday)
    VALUES (source.start_time, source.hour, source.day, source.week, source.month, source.year, source.weekday);
"""

# FIND SONGS

song_select = """
SELECT song_id, s.artist_id 
FROM songs s 
JOIN artists a ON a.artist_id = s.artist_id 
WHERE title = '{}' AND name = '{}';
"""

# QUERY LISTS

create_table_queries = [artist_table_create, user_table_create, time_table_create, song_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]