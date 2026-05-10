-- Lists all cities in the database hbtn_0d_usa with their state names.
SELECT cities.id, cities.name, states.name 
FROM cities, states 
WHERE cities.state_id = states.id 
ORDER BY cities.id ASC;
