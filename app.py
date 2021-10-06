from flask import jsonify

from Infrastructure.constants import app
from Data import database as db


@app.route('/')
def main():
    results = db.query_db("select * from contacts")
    return jsonify({"data": results})


if __name__ == '__main__':
    db.init_db()
    app.run(port=5000)
