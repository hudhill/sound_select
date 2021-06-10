DROP TABLE sources;
DROP TABLE mixes;
DROP TABLE track_lists;

CREATE TABLE sources (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE track_lists (
    id SERIAL PRIMARY KEY, 
    artist VARCHAR(255), 
    song VARCHAR(255)
);

CREATE TABLE mixes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    source_id INT REFERENCES sources(id)
);