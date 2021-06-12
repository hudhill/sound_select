from db.run_sql import run_sql

from models.mix import Mix
import repositories.dj_repository as dj_repository
import repositories.genre_repository as genre_repository

def save(mix):
    sql = "INSERT INTO mixes (title, description, mix_img, tracklist_img, genre_tags, audio_link, genre_id, dj_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    
    genres = genre_repository.select_all()
    genre_names = []
    for genre in genres:
        genre_names.append(genre.name)
        if mix.genre.name == genre.name:
            mix.genre.id = genre.id

    if mix.genre.name not in genre_names:
        genre_repository.save(mix.genre)

    values = [mix.title, mix.description, mix.mix_img, mix.tracklist_img, mix.genre_tags, mix.audio_link, mix.genre.id, mix.dj.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    mix.id = id
    return mix

def select_all():
    mixes = []

    sql = "SELECT * FROM mixes"
    results = run_sql(sql)

    for row in results:
        genre = genre_repository.select(row['genre_id'])
        dj = dj_repository.select(row['dj_id'])
        mix = Mix(row['title'], row['description'], row['mix_img'], row['tracklist_img'], row['genre_tags'], row['audio_link'], genre, dj, row['id'])
        mixes.append(mix)
    return mixes

def select(id):
    mix = None
    sql = "SELECT * FROM mixes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        genre = genre_repository.select(result['genre_id'])
        dj = dj_repository.select(result['dj_id'])
        mix = Mix(result['title'], result['description'], result['mix_img'], result['tracklist_img'], result['genre_tags'], result['audio_link'], genre, dj, result['id'])
    return mix

def delete_all():
    sql = "DELETE FROM mixes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM mixes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(mix):
    sql = "UPDATE mixes SET (title, description, mix_img, tracklist_img, genre_tags, audio_link, genre_id, dj_id) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE ID = %s"
    values = [mix.title, mix.description, mix.mix_img, mix.tracklist_img, mix.genre_tags, mix.audio_link, mix.genre.id, mix.dj.id, mix.id]
    run_sql(sql, values)