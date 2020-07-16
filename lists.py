numbers_list = [1,2,3,4,5]
strings_list = ['a','b','c','d','e']
print(numbers_list[3])
print(strings_list[-1])
#lists methods
numbers_list.append(strings_list)
print(numbers_list)
numbers_list.extend(strings_list)
print(numbers_list)
numbers_list = [34,6,24,5,98,456]
strings_list = ['a','b','c','d','e']
strings_list.reverse()
print(strings_list)
numbers_list.sort()

print(numbers_list)
#matrices
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][2])

# to print diagonal elements
for i in range(0,3):
    print(matrix[i][i])
first_col = [row[0] for row in matrix]
print(first_col)