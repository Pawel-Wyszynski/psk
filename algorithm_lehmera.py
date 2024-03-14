def generate_pseudo_random_numbers(x0, a, m, n):

    xn = x0
    result = []
    sum = 0

    for _ in range(n):
        xn = (a * xn) % m
        sum += xn
        result.append(xn)

    average = (sum/n)/10
    print(average)

    return result