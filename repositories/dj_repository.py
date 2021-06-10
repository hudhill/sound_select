from db.run_sql import run_sql

from models.dj import Dj

def save(dj):
    sql = "INSERT INTO dj (name) VALUES (%s) RETURNING *"
    values = [dj.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    dj.id = id

def select_all():
    djs = []

    sql = "SELECT * FROM djs"
    results = run_sql(sql)

    for row in results:
        dj = Dj(row['name'], row['id'])
        djs.append(dj)

    return djs

def select(id):
    dj = None
    sql = "SELECT * FROM djs WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if len(result) > 0:
        dj_dict = result[0]
        dj = Dj(dj_dict['name'], dj_dict['id'])
    return dj

def delete_all():
    sql = "DELETE FROM djs"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM djs WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(dj):
    sql = "UPDATE djs SET (name) = (%s) WHERE ID = %s"
    values = [dj.name, dj.id]
    run_sql(sql, values)