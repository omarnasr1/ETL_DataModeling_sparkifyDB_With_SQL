## creating a database schema and ETL pipeline for `Sparkify`.
I have 2 types of `JSON files` the first one has data about the `song` and the `artist` and the second one has data about the `sessions` itself, I will use those 2 files to create a database whiche contains 5 tables

#### Project Repository files:
- sql_queries.py
contains all the `sql queries`, it will be used in the other files.
- create_tables.py 
drops and creates tables.
- etl.ipynb 
reads and processes `files` from `song_data` and `log_data` and loads them into the tables.


#### ETL Process
we have 2 directory 
- log_data it contains log files in JSON format describes the action happened in the sessions, in the page NextSong you can find some data about the song played by the user 
- song_data it contains log files in JSON format have specific data about the song
- we will use the song_data files to build the songs and artists table
- we will use the log_data files to build the rest of the tables


###### Fact Table

- songplays - records in log data associated with song plays i.e. records with page NextSong 
    songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

###### Dimension Tables

- users - users in the app
        user_id, first_name, last_name, gender, level
- ongs - songs in music database
        song_id, title, artist_id, year, duration
- artists - artists in music database
        artist_id, name, location, latitude, longitude
- time - timestamps of records in songplays broken down into specific units
        start_time, hour, day, week, month, year, weekday
        
