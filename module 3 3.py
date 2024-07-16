def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params(b = 5)
print_params(c = [1, 2, 3])

value_list = [2, 'подстрока', False]
value_dict = {'a':'start', 'b':'stop', 'c':'finish'}
value_list_2 = [54.32, 'Строка']

print_params(*value_list)
print_params(**value_dict)
print_params(*value_list_2, 42)





