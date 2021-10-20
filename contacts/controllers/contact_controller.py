from flask import request

from data.controller.database_controller import *

TABLE = 'contacts'
COLUMNS = ['first_name', 'last_name', 'email', 'phone']


class ContactController:

    @staticmethod
    def get_all_contacts():
        return build_get_all(TABLE)()

    @staticmethod
    def get_contact_by_id(id):
        return build_get_by_id(TABLE)(id)

    @staticmethod
    def create_contact():
        return build_create(TABLE, COLUMNS, [request.json[key] for key in COLUMNS])()

    @staticmethod
    def delete_contact_by_id(id):
        return build_delete(TABLE)(id)

    @staticmethod
    def update_contact(id):
        return build_update(TABLE, COLUMNS, [request.json[key] for key in COLUMNS])(id)

    @staticmethod
    def update_contact_by_id(id):
        return build_update_by_id(TABLE, COLUMNS, request)(id)

    @staticmethod
    def delete_all_contacts(id):
        pass
