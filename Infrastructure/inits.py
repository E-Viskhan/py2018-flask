from Infrastructure.methods_name import *
from Infrastructure.constants import *
from Infrastructure.routes import ROUTES as routes

from Contacts.View import view as contacts_view


def init_urls():

    # Contacts urls register
    app.add_url_rule(routes['contacts'], view_func=contacts_view.get_contacts, methods=GET)
    app.add_url_rule(routes['contacts'], view_func=contacts_view.create_contact, methods=POST)
    app.add_url_rule(build_path_with_args(routes['contacts'], '<int:id>'), view_func=contacts_view.delete_contact, methods=DELETE)
