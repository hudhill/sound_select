from db.run_sql import run_sql

from models.source import Source

def save(source):
    sql = "INSERT INTO sources (name) VALUES (%s) RETURNING *"
    values = [source.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    source.id = id

def select_all():
    sources = []

    sql = "SELECT * FROM sources"
    results = run_sql(sql)

    for row in results:
        source = Source(row['name'], row['id'])
        sources.append(source)

    return sources

def select(id):
    source = None
    sql = "SELECT * FROM sources WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if len(result) > 0:
        source_dict = result[0]
        source = Source(source_dict['name'], source_dict['id'])
    return source

def delete_all():
    sql = "DELETE FROM sources"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM sources WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(source):
    sql = "UPDATE sources SET (name) = (%s) WHERE ID = %s"
    values = [source.name, source.id]
    run_sql(sql, values)