class Contact:
    def __init__(self, name, sur_name, email, phone_number):
        self.name = name
        self.surName = sur_name
        self.email = email
        self.phoneNumber = phone_number

    def get_full_name(self): return f"{self.name} {self.surName}"
