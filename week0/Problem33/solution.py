def magic_square(matrix):
    n = len(matrix)
    M = (n * (n * 2 + 1)) / 2
    l = []
    d1 = []
    d2 = []
    for i in range(0, len(matrix)):
        l.append([item[i] for item in matrix])
        d1.append(matrix[i][i])
        d2.append(matrix[i][n - 1 - i])
    l = matrix + l + [d1] + [d2]

    l = list(map(lambda x: sum(x), l))
    l.append(M)
    return all(l)
