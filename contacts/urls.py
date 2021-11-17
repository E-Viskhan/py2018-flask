from contacts.controllers.contact_controller import ContactController
from infrastructure.methods_name import *


class Url:
    def __init__(self, path, view, methods):
        self.path = path
        self.view = view
        self.methods = methods


urls = [
    Url('/contacts', ContactController.get_all_contacts, [GET]),
    Url('/contacts/<int:id>', ContactController.get_contact_by_id, [GET]),
    Url('/contacts', ContactController.create_contact, [POST]),
    Url('/contacts/<int:id>', ContactController.replace_contact, [PUT]),
    Url('/contacts/<int:id>', ContactController.update_contact, [PATCH]),
    Url('/contacts/<int:id>', ContactController.delete_contact_by_id, [DELETE]),
]
