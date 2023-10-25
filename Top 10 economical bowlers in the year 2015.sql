-- select the bowler and find the economy by the formula
SELECT bowler, SUM(total_runs)/((COUNT(ball))/6) AS economy
-- select the dataset
FROM cricket_match
-- for year 2015 match id is from 1 to 59 
WHERE match_id > 0 AND match_id < 60
-- group by bowlers 
GROUP BY bowler
-- order for the best on top 
order by economy;

-- sample output--

      bowler       | economy 
-------------------+---------
 NB Singh          |       4
 R Tewatia         |       5
 Mohammad Nabi     |       5
 KH Pandya         |       6
 LH Ferguson       |       6
 Harbhajan Singh   |       6
 Avesh Khan        |       6
 SP Narine         |       6
 Rashid Khan       |       6
 AJ Tye            |       6
 GJ Maxwell        |       6
 S Nadeem          |       6
 Washington Sundar |       6

