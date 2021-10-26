from flask import jsonify
from Data.database import query_db, mutate_db


def build_create(table, columns, data):
    def create():
        values = ', '.join(['?' for _ in columns])
        names = ', '.join([name for name in columns])
        query = f"INSERT INTO {table}({names}) VALUES({values})"
        id = mutate_db(query, data)

        return jsonify({"id": id})

    return create


def build_get_all(table):
    def get_all():
        items = query_db(f'SELECT * FROM {table}')
        return jsonify(items)

    return get_all


def build_get_by_id(table):
    def get_by_id(id):
        item = query_db(f'SELECT * FROM {table} WHERE id = ?', (id,), one=True)
        return jsonify(item)

    return get_by_id


def build_replace(table, columns, values):
    def update(id):
        sets = ", ".join([f"{key} = ?" for key in columns])
        # values = [request.form[key] for key in columns]
        mutate_db(f"UPDATE {table} SET {sets} WHERE id = ?", (*values, id))
        return jsonify({"id": id})

    return update


def build_update(table, columns, request):
    def patch(id):
        sets = ",".join([f"{key} = ?" for key in request.json.keys() if key in columns])
        # values = [value for key, value in request.form.items() if key in columns]
        values = [request.json[key] for key in request.json.keys() if key in columns]
        mutate_db(f"UPDATE {table} SET {sets} WHERE id = ?", (*values, id,))
        item = query_db(f'SELECT * FROM {table} WHERE id = ?', (id,), one=True)
        return jsonify(item)

    return patch


def build_delete(table):
    def delete_by_id(id):
        mutate_db(f"DELETE FROM {table} WHERE id = ?", (id,))
        return jsonify(f'Запись с id: {id} удалена')

    return delete_by_id
