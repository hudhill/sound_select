from db.run_sql import run_sql

from models.genre import Genre

def save(genre):
    sql = "INSERT INTO genres (name) VALUES (%s) RETURNING *"
    values = [genre.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    genre.id = id

def select(id):
    genre = None
    sql = "SELECT * FROM genres WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if len(result) > 0:
        genre_dict = result[0]
        genre = Genre(genre_dict['name'], genre_dict['id'])
    return genre