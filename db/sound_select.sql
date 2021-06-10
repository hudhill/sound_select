DROP TABLE djs;
DROP TABLE mixes;
DROP TABLE track_lists;

CREATE TABLE djs (
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
    title VARCHAR(255),
    description TEXT,
    dj_id INT REFERENCES djs(id)
);