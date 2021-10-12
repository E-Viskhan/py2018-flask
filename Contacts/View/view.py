from Contacts.Controllers.contact_controller import ContactController

controller = ContactController()


def all_contacts():
    return controller.get_all_contacts()


def contact_by_id(id):
    return controller.get_contact_by_id(id)


def create_contact():
    return controller.create_contact()


def update_contact():
    pass


def delete_contact(id: int):
    return {'': 'log'}
