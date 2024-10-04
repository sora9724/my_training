def print_params(a = 1, b = 'строка', c = True):
    print(a, b ,c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
values_list = [12.34, False, 'strinig']
values_dict = {'a': 56, 'b': 'string', 'c': True}
print_params(*values_list)
print_params(**values_dict)
values_list2 = [14.57, False]
print_params(*values_list2, 42)
