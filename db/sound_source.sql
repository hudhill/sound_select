DROP TABLE IF EXISTS djs;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS mixes;

CREATE TABLE djs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    img VARCHAR(255)
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    color VARCHAR(255)
);

CREATE TABLE mixes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    mix_img VARCHAR(255),
    tracklist_img VARCHAR(255),
    genre_tags VARCHAR(255),
    audio_link VARCHAR(255),
    mysource BOOLEAN,
    genre_id INT REFERENCES genres(id),
    dj_id INT REFERENCES djs(id) ON DELETE CASCADE
);