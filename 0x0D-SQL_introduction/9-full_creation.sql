-- creates a table with id-name-score
-- id as int and name as string and score as int
-- insetrs four rows
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14),
(4, 'George', 8)
