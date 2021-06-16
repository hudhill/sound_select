from db.run_sql import run_sql

from models.genre import Genre

def save(genre):
    sql = "INSERT INTO genres (name, color) VALUES (%s, %s) RETURNING *"
    values = [genre.name, genre.color]
    results = run_sql(sql, values)
    id = results[0]['id']
    genre.id = id

def select_all():  # in use in mixes controller
    genres = []

    sql = "SELECT * FROM genres"
    results = run_sql(sql)

    for row in results:
        genre = Genre(row['name'], row['color'], row['id'])
        genres.append(genre)

    return genres

def select(id):
    genre = None
    sql = "SELECT * FROM genres WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if len(result) > 0:
        genre_dict = result[0]
        genre = Genre(genre_dict['name'], genre_dict['color'], genre_dict['id'])
    return genre

def delete_all():  # in use in console
    sql = "DELETE FROM genres"
    run_sql(sql)