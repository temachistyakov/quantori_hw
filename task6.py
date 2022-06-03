def print_spiral(x: int):
    cnt = 1
    iteration = 0
    size = x
    result = [[0] * x for i in range(x)]
    while cnt <= x**2:
        for i in range(iteration, x - iteration):
            result[iteration][i] = cnt
            result[x - 1 - iteration][x - i - 1] = cnt + 2 * (size - 1)
            cnt += 1
        size -= 2
        if cnt != x**2:
            for j in range(iteration, iteration + size):
                result[j + 1][x - 1 - iteration] = cnt
                result[x - j - 2][iteration] = cnt + 2 * (size + 1)
                cnt += 1
            cnt = cnt + 2 * (size + 1)
        iteration += 1
    for i in range(x):
        print(result[i])

print_spiral(5)
