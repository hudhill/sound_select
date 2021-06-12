DROP TABLE djs;
DROP TABLE genres;
DROP TABLE mixes;

CREATE TABLE djs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    bio TEXT  -- need to get these
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE mixes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    mix_img VARCHAR(255),
    tracklist_img VARCHAR(255),
    genre_tags VARCHAR(255),
    audio_link VARCHAR(255),
    genre_id INT REFERENCES genres(id),
    dj_id INT REFERENCES djs(id)
);