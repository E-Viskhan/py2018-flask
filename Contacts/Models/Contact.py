class Contact:
    def __init__(self, id, name, sur_name, email, phone_number):
        self.id = id
        self.name = name,
        self.surName = sur_name
        self.phoneNumber = phone_number

    def get_full_name(self): return f"{self.name, self.surName}"
