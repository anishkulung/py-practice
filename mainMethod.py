import property_decorators
print(property_decorators.__name__)
print(__name__)
def __str__():
	return ( 'This is {} function'.format(__name__))
def __repr__():
	return ( 'This is {} function'.format(__name__))
if __name__ == '__main__':
	s = __str__()
	r = __repr__()
print(s)
print(r)