-- choose the batting to calculate the run and add the extra runs 
select batting_team as team,sum(extra_runs) 
-- select the datset 
from cricket_match 
join the data set for finding the year 
inner join data 
        on cricket_match.match_id = data.id 
-- condintion for the year
where season = 2016
-- group by team for calcation acording to teams
group by team

---output-- 

/*
            team             | sum 
-----------------------------+-----
 Kolkata Knight Riders       | 130
 Rising Pune Supergiants     | 101
 Mumbai Indians              | 102
 Delhi Daredevils            | 109
 Kings XI Punjab             |  83
 Royal Challengers Bangalore | 118
 Gujarat Lions               | 132
 Sunrisers Hyderabad         | 124

*/
