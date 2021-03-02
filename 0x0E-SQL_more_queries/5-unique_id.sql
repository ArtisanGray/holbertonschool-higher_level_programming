-- creates a table with unique values enforced.
-- noticed that mySQL uses different nomenclature/structure.
CREATE TABLE IF NOT EXISTS 'unique_id' (
	id INT NOT NULL DEFAULT 1,
	name VARCHAR (256),
	UNIQUE (id)
);
