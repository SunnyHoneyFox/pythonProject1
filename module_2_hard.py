def generate_pairs(n):
    pairs = []
    for i in range(1, n):
        for j in range(i, n):
            if i != j and i != n and j != n and n % (i + j) == 0:
                pairs.append((i, j))
    return pairs

def generate_result(n, pairs):
    result = ""
    for pair in pairs:
        result += str(pair[0]) + str(pair[1])
    return result

n = int(input())
pairs = generate_pairs(n)
result = generate_result(n, pairs)
print(result)







