from db.run_sql import run_sql

from models.mix import Mix
import repositories.source_repository as source_repository

def save(mix):
    sql = "INSERT INTO mixes (name, description, source_id) VALUES (%s, %s, %s) RETURNING *"
    values = [mix.name, mix.description, mix.source.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    mix.id = id
    return mix

def select_all():
    mixes = []

    sql = "SELECT * FROM mixes"
    results = run_sql(sql)

    for row in results:
        source = source_repository.select(row['source_id'])
        mix = Mix(row['name'], row['description'], source, row['id'])
        mixes.append(mix)
    return mixes

def select(id):
    mix = None
    sql = "SELECT * FROM mixes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        source = source_repository.select(result['source_id'])
        mix = Mix(result['name'], result['description'], source, result['id'])
    return mix

def delete_all():
    sql = "DELETE FROM mixes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM mixes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(mix):
    sql = "UPDATE mixes SET (name, description, source_id) = (%s, %s, %s) WHERE ID = %s"
    values = [mix.name, mix.description, mix.source.id, mix.id]
    run_sql(sql, values)