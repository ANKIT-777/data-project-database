postgres=# 
-- imported umpires data set as 'umpires'
SELECT Country, COUNT(UmpireName) AS UmpireCount
-- selecting row from the copied dataset
FROM Umpires
--checking if country is not india
WHERE Country NOT LIKE '%India'
--groupping by country 
GROUP BY Country


-- output :
    country    | umpirecount 
---------------+-------------
  Australia    |           7
  South Africa |           5
  New Zealand  |           4
  England      |           3
  Sri Lanka    |           2
  Pakistan     |           2
  West Indies  |           1
  Zimbabwe     |           1


