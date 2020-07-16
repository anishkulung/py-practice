class Employee:

	raise_amount = 1.02
	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.email = fname + lname + '@mail.com'
		self.pay = pay

	def full_name(self):
		return 'fullname:{} {}'.format(self.fname,self.lname)

	def pay_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		return self.pay

	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.fname,self.lname, self.pay)

	def __str__(self):
		return "{} - {}".format(self.full_name(),self.email)


emp1 = Employee('Anish','Rai',40000)
emp2 = Employee('Romeo','Rai',90000)

print(emp1)
print(str(emp1))
print(emp1.__str__())
print(repr(emp1))
print(emp1.__repr__())