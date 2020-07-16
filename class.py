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

    @classmethod
    def set_raiseAmt(cls, amount):
        cls.raise_amount = amount

    # classmethod working as constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)


emp1 = Employee("Anish", "Rai", 40000)
print(emp1.full_name())
print(emp1.pay_raise())
print(emp1.raise_amount)
emp1.set_raiseAmt(1.05)
print(emp1.raise_amount)
print(emp1.pay_raise())


# emp_str = "John-Doe-20000"
# new_emp = Employee.from_string(emp_str)
# print(new_emp.full_name())
# print(dir(new_emp))
# print(new_emp.raise_amount)
# new_emp.set_raiseAmt(1.10)
# print(new_emp.raise_amount)

