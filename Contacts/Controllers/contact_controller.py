from flask import jsonify, request

from Data.Controller.DatabaseController import *
from Contacts.Models.Contact import Contact

TABLE = 'contacts'
COLUMNS = ['first_name', 'last_name', 'email', 'phone']


class ContactController:
    contact = Contact

    def init_model(self):
        name, last_name, email, phone = request.args['firstName'], request.args['lastName'], request.args['email'], request.args['phone']
        _contact = Contact(name, last_name, email, phone)
        self.contact = _contact

        return _contact

    def get_all_args(self):
        return [self.contact.name, self.contact.surName, self.contact.email, self.contact.phoneNumber]

    @staticmethod
    def get_all_contacts():
        return build_get_all(TABLE)

    @staticmethod
    def get_contact_by_id(id):
        return build_get_by_id(TABLE)(id)

    def create_contact(self):
        self.init_model()
        return build_create(TABLE, COLUMNS, self.get_all_args())

    @staticmethod
    def delete_contact_by_id(id):
        pass

    @staticmethod
    def update_contact_by_id(id):
        pass

    @staticmethod
    def delete_all_contacts(id):
        pass
