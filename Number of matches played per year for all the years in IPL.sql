-- Number of matches played per year for all the years in IPL.

postgres=# 
-- selected season and renamed for better understanding counting number of years in the dataset 
SELECT season as Year, COUNT(season) as matches_this_year 
--our dataset 'data'
FROM data 
--group them by year and order them for better understanding 
GROUP BY season Order by season;

---- 
--output :

year | matches_this_year 
------+-------------------
 2008 |                58
 2009 |                57
 2010 |                60
 2011 |                73
 2012 |                74
 2013 |                76
 2014 |                60
 2015 |                59
 2016 |                60
 2017 |                59
(10 rows)
