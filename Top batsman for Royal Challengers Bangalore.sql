-- sum up all the runs by the each batsman , and keep the name of batsman side by side
SELECT SUM(batsman_runs) AS TotalRuns, batsman
-- select the dataset 
FROM Cricket_Match
--specify the team name
WHERE batting_team LIKE '%Royal Challengers Bangalore'
-- group by the batsmans to have distinct values
GROUP BY batsman 
--order by highest to lowest
order by totalruns desc 
-- for taking the top of the highest
limit 10;

-- output -- 

 totalruns |    batsman     
-----------+----------------
      4423 | V Kohli
      3175 | CH Gayle
      2815 | AB de Villiers
      1132 | JH Kallis
       898 | R Dravid
       587 | TM Dilshan
       549 | RV Uthappa
       517 | LRPL Taylor
       487 | SS Tiwary
       433 | MA Agarwal

