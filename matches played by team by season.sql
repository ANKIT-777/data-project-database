-- Select the season as Year, team, and count of matches played
SELECT season AS Year, team, COUNT(*) AS matches_played
FROM (
    -- Create a subquery that combines team1 for each match and associates it with the season
    SELECT season, team1 AS team
    FROM data
    UNION ALL
    -- Union the subquery with team2 for each match and associate it with the season
    SELECT season, team2 AS team
    FROM data
) AS subquery
-- Group the result by season and team
GROUP BY season, team
-- Order the final result by season and team
ORDER BY season, team;


ex : output :- 
 year |            team             | matches_played 
------+-----------------------------+----------------
 2008 | Chennai Super Kings         |             16
 2008 | Deccan Chargers             |             14
 2008 | Delhi Daredevils            |             14
 2008 | Kings XI Punjab             |             15
 2008 | Kolkata Knight Riders       |             13
 2008 | Mumbai Indians              |             14
 2008 | Rajasthan Royals            |             16
 2008 | Royal Challengers Bangalore |             14
 2009 | Chennai Super Kings         |             14
 2009 | Deccan Chargers             |             16
 2009 | Delhi Daredevils            |             15
 2009 | Kings XI Punjab             |             14
 2009 | Kolkata Knight Riders       |             13
 2009 | Mumbai Indians              |             13
 2009 | Rajasthan Royals            |             13
 2009 | Royal Challengers Bangalore |             16
 2010 | Chennai Super Kings         |             16
 2010 | Deccan Chargers             |             16
 2010 | Delhi Daredevils            |             14
 2010 | Kings XI Punjab             |             14
 2010 | Kolkata Knight Riders       |             14
 2010 | Mumbai Indians              |             16
 2010 | Rajasthan Royals            |             14
