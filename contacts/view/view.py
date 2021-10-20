from contacts.controllers.contact_controller import ContactController

controller = ContactController()


def all_contacts():
    return controller.get_all_contacts()


def contact_by_id(id):
    return controller.get_contact_by_id(id)


def create_contact():
    return controller.create_contact()


def update_contact(id):
    return controller.update_contact(id)


def update_contact_by_id(id):
    return controller.update_contact_by_id(id)


def delete_contact(id):
    return controller.delete_contact_by_id(id)
