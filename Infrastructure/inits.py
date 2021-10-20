from infrastructure.methods_name import *
from infrastructure.constants import *
from infrastructure.routes import routes

from contacts.view import view as contacts_view


def init_urls():

    # contacts urls register
    app.add_url_rule(routes['contacts'], view_func=contacts_view.all_contacts, methods=GET)
    app.add_url_rule(routes['contacts'], view_func=contacts_view.create_contact, methods=POST)
    app.add_url_rule('/contacts/<int:id>', view_func=contacts_view.update_contact, methods=PUT)
    app.add_url_rule('/contacts/<int:id>', view_func=contacts_view.update_contact_by_id, methods=PATCH)
    app.add_url_rule('/contacts/<int:id>', view_func=contacts_view.delete_contact, methods=DELETE)
