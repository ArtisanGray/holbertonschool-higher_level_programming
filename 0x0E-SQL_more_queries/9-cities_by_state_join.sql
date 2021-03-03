-- lists all cities in the database.
-- uses inner join to return all matches
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id=states.id;
