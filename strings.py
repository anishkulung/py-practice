string = "Hello Anish"

#string indexing
print(string[6])

#negative slicing
print(string[-1])
print(string[-(len(string)):])

#string slicing
print(string[:3])
print(string[4:8])
print(string[::])
print(string[::9])

print(string[::3])

#string methods
x = string.upper()
print(x)
x = string.lower()
print(x)
x = string.capitalize()
print(x)
#spliting string with reference to space(character) 
x = string.split()
print(x)
#spliting string with reference to character "e"
x = string.split('e')
print(x)
print(string.split('l'))


#print formatting
print('this is my first program in {}'.format('python'))
x = 'My name is {x}. I am a {y}'.format(x='anish',y = 'programmer')
print(x)
