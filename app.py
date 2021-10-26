from infrastructure.constants import app
from infrastructure.router import init_urls
from data import database as db

from contacts.schema.schema import schema_path as contacts_schema_path

if __name__ == '__main__':
    db.schema_paths.append(contacts_schema_path)
    db.init_db()
    init_urls()
    app.run(debug=True, port=8000)
