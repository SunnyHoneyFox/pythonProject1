calls = 0
def count_calls():
    global calls
    calls += 1
    return

def string_info(string):
    count_calls()
    length = str(len(string))
    big = string.upper()
    small = string.lower()
    launch = (int(length), big, small)
    return launch

def is_contains(string1, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() == string1.lower():
            itogo = True
            break
        else:
            itogo = False
    return itogo

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print((calls))





