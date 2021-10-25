from infrastructure.base_controller import BaseController

TABLE = 'contacts'
COLUMNS = ['first_name', 'last_name', 'email', 'phone']


class ContactController(BaseController):

    @classmethod
    def get_all_contacts(cls):
        return super().get_all(TABLE)

    @classmethod
    def get_contact_by_id(cls, id):
        return super().get_by_id(TABLE, id)

    @classmethod
    def create_contact(cls):
        return super().create(TABLE, COLUMNS)

    @classmethod
    def delete_contact_by_id(cls, id):
        return super().delete_by_id(TABLE, id)

    @classmethod
    def replace_contact(cls, id):
        return super().replace(TABLE, COLUMNS, id)

    @classmethod
    def update_contact(cls, id):
        return super().update(TABLE, COLUMNS, id)

    @classmethod
    def delete_all_contacts(cls, id):
        pass
