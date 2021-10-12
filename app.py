from flask import jsonify

from Infrastructure.constants import app
from Infrastructure.routes import routes
from Infrastructure.inits import init_urls
from Data import database as db


@app.route(routes['home'])
def main():
    return jsonify('Hello world')


if __name__ == '__main__':
    db.init_db()
    init_urls()
    app.run(debug=True, port=5000)
