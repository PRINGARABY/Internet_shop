

Class User:
def __init__(self, id, fio, password, phone, email):
self.id = id
self.fio = fio
self.password = password
self.phone = phone
self.email = email
def login(self):
    pass
def logout(self)
    pass
def update_profile(self)
    pass

class Client(User):
    def __init__(self, address, bonus_points):
        self.adress = aadress
        self.bonus_points = bonus_points
    def view_catalog(sself):
        pass
    def find_product(self):
        pass
    def make_order(self):
        pass
    def ask_quesion(self):
        pass
    def add_review(sel):
        pass

class Employee(User):
    def __init__(self, personnel_number, position, hire_date):
       self.personnel_number = personnel_number
       self.position = position
       self.hire_date = hire_date
    def resign(self):
        pass

class Admin(Emploee):
    def add_product(self):
        pass
    def delete_product(self):
        pass
    def update_product(self):
        pass
