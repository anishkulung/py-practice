class Employee:

    raise_amount = 1.02

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def full_name(self):
        return "fullname:{} {}".format(self.fname, self.lname)

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay


class Developer(Employee):
    raise_amount = 1.05

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.full_name())


dev1 = Developer("Anish", "Rai", 50000, "python")
dev2 = Developer("akr", "Rai", 50000, "python")
print(dev1.full_name())
print(dev1.prog_lang)

mngr1 = Manager("Romeo", "Rai", 80000)

mngr1.add_emp(dev1)
mngr1.add_emp(dev2)
mngr1.print_emp()
