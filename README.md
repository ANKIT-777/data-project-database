
# Load CSV
  Write a SQL script that loads CSV data into a table.

##- Made Table "Data"
*postgres=# CREATE TABLE Data (
    id integer,
    season integer,
    city text,
    date date,
    team1 text,
    team2 text,
    toss_winner text,
    toss_decision text,
    result text,
    dl_applied integer,
    winner text,
    win_by_runs integer,
    win_by_wickets integer,
    player_of_match text,
    venue text,
    umpire1 text,
    umpire2 text,
    umpire3 text
);*

## - now copies data to my table
  
*postgres=# \COPY Data FROM '/Users/ankitsharma/Desktop/Python/IPL/matches.csv' DELIMITER ',' CSV HEADER;*  

