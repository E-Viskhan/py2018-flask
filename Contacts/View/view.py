from flask import request, jsonify
from Data import database as db


def get_contacts():
    results = db.query_db("select * from contacts")
    return jsonify({"data": results})


def create_contact():
    arguments = request.args
    query = f"INSERT INTO contacts(first_name, last_name, email, phone) VALUES(?, ?, ?, ?)"
    return {'': query}


def delete_contact(id: int):
    return {'': 'log'}
