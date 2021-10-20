from data.database import query_db, mutate_db


def build_create(table, columns, data):
    def create():
        values = ', '.join(['?' for _ in columns])
        names = ', '.join([name for name in columns])
        query = f"INSERT INTO {table}({names}) VALUES({values})"
        id = mutate_db(query, data)

        return {"id": id}

    return create()


def build_get_all(table):
    def get_all():
        items = query_db(f'SELECT * FROM {table}')
        return {"data": items}

    return get_all


def build_get_by_id(table):
    def get_by_id(id):
        item = query_db(f'SELECT * FROM {table} WHERE id = ?', (id,), one=True)
        return {"data": item}

    return get_by_id


def build_update(table, columns, values):
    def update(id):
        sets = ", ".join([f"{key} = ?" for key in columns])
        # values = [request.form[key] for key in columns]
        mutate_db(f"UPDATE {table} SET {sets} WHERE id = ?", (*values, id))
        return {"id": id}

    return update


def build_update_by_id(table, columns, request):
    def patch(id):
        sets = ",".join([f"{key} = ?" for key in request.form.keys() if key in columns])
        values = [value for key, value in request.form.items() if key in columns]
        mutate_db(f"UPDATE {table} SET {sets} WHERE id = ?", (*values, id,))
        return {"id": id}

    return patch


def build_delete(table):
    def delete_by_id(id):
        mutate_db(f"DELETE FROM {table} WHERE id = ?", (id,))
        return {"id": id}

    return delete_by_id
