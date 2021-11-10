import sqlite3

from flask import g
from infrastructure.constants import *


schema_paths = []


def init_db():
    with app.app_context():
        db = get_db()
        for schema_path in schema_paths:
            with app.open_resource(schema_path, mode='r') as f:
                db.cursor().executescript(f.read())
        db.commit()


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE, check_same_thread=False)
        db.row_factory = make_dicts
    return db


def query_db(query, args=(), one=False):
    cur = None
    try:
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
    finally:
        if cur:
            cur.close()
    return (rv[0] if rv else None) if one else rv


def mutate_db(query, args=()):
    cur = None
    try:
        db = get_db()
        cur = db.execute(query, args)
        db.commit()
    finally:
        if cur:
            cur.close()
    return cur.lastrowid


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
