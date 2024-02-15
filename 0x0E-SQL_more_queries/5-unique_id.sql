-- creates table unique_id which have constrain id UNIQUE
CREATE TABLE IF NOT EXISTS unique_id (
		id INT DEFAULT 1 UNIQUE,
		name VARCHAR(256)
		);
