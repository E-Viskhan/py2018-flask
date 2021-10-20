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

    def create_contact(self):
        return build_create(TABLE, COLUMNS, [request.json[key] for key in COLUMNS])

    @staticmethod
    def delete_contact_by_id(id):
        pass

    @staticmethod
    def update_contact_by_id(id):
        pass

    @staticmethod
    def delete_all_contacts(id):
        pass
