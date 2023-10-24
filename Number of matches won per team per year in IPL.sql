postgres=# 
-- renamed the 'season' as 'year', 'winner' as 'team' for better understanding and found
--count the number of wins for each team in each season.
SELECT season AS year, winner AS team, COUNT(winner) AS total_wins

-- Group the data by 'season' and 'winner' to get the count of wins per team per year.
FROM data

-- Group the data by 'season' and 'winner'.
GROUP BY season, winner

  -- Order the results by 'season' and 'winner' for a structured output.
ORDER BY season, winner;



--output example
 year |            team             | total_wins 
------+-----------------------------+------------
 2008 | Chennai Super Kings         |          9
 2008 | Deccan Chargers             |          2
 2008 | Delhi Daredevils            |          7
 2008 | Kings XI Punjab             |         10
 2008 | Kolkata Knight Riders       |          6
 2008 | Mumbai Indians              |          7
 2008 | Rajasthan Royals            |         13
 2008 | Royal Challengers Bangalore |          4
 2009 | Chennai Super Kings         |          8
 2009 | Deccan Chargers             |          9
 2009 | Delhi Daredevils            |         10
 2009 | Kings XI Punjab             |          7
 2009 | Kolkata Knight Riders       |          3
 2009 | Mumbai Indians              |          5
 2009 | Rajasthan Royals            |          6
