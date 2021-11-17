from infrastructure.base_controller import BaseController


class ContactController(BaseController):
    TABLE = 'contacts'
    COLUMNS = ['first_name', 'last_name', 'email', 'phone']

