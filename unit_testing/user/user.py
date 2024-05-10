class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()

    @property
    def email(self):
        first_name = self.first_name.lower()
        last_name = self.last_name.lower()
        return f"{first_name}_{last_name}@email.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
