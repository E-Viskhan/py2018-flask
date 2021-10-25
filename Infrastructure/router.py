from infrastructure.constants import app
from contacts.urls import urls as contact_url


def init_urls():
    for url in contact_url:
        app.add_url_rule(url.path, view_func=url.view, methods=url.methods)
