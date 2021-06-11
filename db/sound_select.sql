DROP TABLE djs;
DROP TABLE mixes;

CREATE TABLE djs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    bio TEXT  -- need to get these
);

CREATE TABLE mixes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    mix_img VARCHAR(255),
    tracklist_img VARCHAR(255),
    genres VARCHAR(255),
    -- soundlcoud link
    dj_id INT REFERENCES djs(id)
);

-- CREATE TABLE genres (
--     id SERIAL PRIMARY KEY,
--     genre VARCHAR(255),
--     mix_id INT REFERENCES mixes(id)
-- );