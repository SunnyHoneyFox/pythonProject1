def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    print(a, c)
    print(b)
    print()

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

value_list = [2, 3.4, 'odin']
value_dict = {'a':'start', 'b':3, 'c': 1.5}
value_list_2 = [1, 2.3]

print_params(*value_list)
print_params(**value_dict)
print_params(*value_list_2, "lol")





