class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return self.first + '.' + self.last + '@gmail.com'

    @fullname.setter
    def fullname(self,full_name):
        first_name, last_name = full_name.split(" ")
        self.first = first_name
        self.last = last_name

    @fullname.deleter
    def fullname(self):
        print('Full name deleted')
        self.first = None
        self.last = None


employee_1 = Employee('Andrés', 'López')
print("=== CHANGE 0 ===")
print(employee_1.fullname)
print(employee_1.email)

print("=== CHANGE 1 ===")
employee_1.fullname = "Marco Velázquez"
print(f"full name: {employee_1.fullname}")
print(f"first name: {employee_1.first}")
print(f"last name: {employee_1.last}")
print(f"email: {employee_1.email}")

print("=== AFTER DELETING ==")
del employee_1.fullname
print(f"full name: {employee_1.fullname}")
print(f"first name: {employee_1.first}")
print(f"last name: {employee_1.last}")