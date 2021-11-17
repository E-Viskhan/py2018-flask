from contacts.controllers.contact_controller import ContactController
from infrastructure.methods_name import *


class Url:
    def __init__(self, path, view, methods):
        self.path = path
        self.view = view
        self.methods = methods


urls = [
    Url('/contacts', ContactController.get_all, GET),
    Url('/contacts/<int:id>', ContactController.get_by_id, GET),
    Url('/contacts', ContactController.create, POST),
    Url('/contacts/<int:id>', ContactController.replace_by_id, PUT),
    Url('/contacts/<int:id>', ContactController.update_by_id, PATCH),
    Url('/contacts/<int:id>', ContactController.delete_by_id, DELETE),
]
