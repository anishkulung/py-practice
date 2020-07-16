
class Employee():
	"""docstring for Employee"""
	def __init__(self, fname, lname):
			self.fname = fname
			self.lname = lname
	@property
	def	email(self):
		return '{}{}@mail.com'.format(self.fname, self.lname)

	@property
	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)

	@fullname.setter
	def fullname(self, name):
		fname, lname = name.split(' ')
		self.fname = fname
		self.lname = lname

	@fullname.deleter
	def fullname(self):
		print('Delete name')
		self.fname = None
		self.lname = None 

emp1 = Employee('Anish', 'Rai')
print(emp1.fullname)
del emp1.fullname
emp1.fullname = 'Romeo Rai'
print(emp1.fullname)
print(emp1.email)
