def sum_num_and_len(data_structure):
    total_num = 0
    total_len = 0

    for i in data_structure:
        if isinstance(i, (int, float)):
            total_num += i
        elif isinstance(i, str):
            total_len += len(i)
        elif isinstance(i, (list, tuple, set)):
            for j in i:
                total_num2, total_len2 = sum_num_and_len([j])
                total_num += total_num2
                total_len += total_len2
        elif isinstance(i, dict):
            for key, value in i.items():
                total_num2, total_len2 = sum_num_and_len([key, value])
                total_num += total_num2
                total_len += total_len2

    return total_num, total_len


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_num, total_len = sum_num_and_len(data_structure)

print(total_len + total_num)
