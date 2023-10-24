select batting_team,sum(total_runs) as Total_run  
-- Select the batting team and calculate the total runs using the SUM function.
from Cricket_Match 

group by batting_team;
-- Group the results by the batting team to calculate the total runs for each team.

--output:--

        batting_team         | total_run 
-----------------------------+-----------
 Kolkata Knight Riders       |     21965
 Rising Pune Supergiants     |      2063
 Pune Warriors               |      6358
 Royal Challengers Bangalore |     23436
 Kochi Tuskers Kerala        |      1901
 Rising Pune Supergiant      |      2470
 Mumbai Indians              |     24521
 Chennai Super Kings         |     20899
 Delhi Daredevils            |     21953
 Kings XI Punjab             |     23068
 Rajasthan Royals            |     17703
 Deccan Chargers             |     11463
 Gujarat Lions               |      4862
 Sunrisers Hyderabad         |     11652
(14 rows)



