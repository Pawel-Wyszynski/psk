def middle_square(seed):
    s = str(seed ** 2)
    while len(s) != 8:
        s = "0" + s
    seed = int(s[2:6])
    return seed

def von_neumann(seed,iteration):
    sum = 0
    for i in range(0,iteration):
        sum += seed
        print(middle_square(seed))
        seed = middle_square(seed)
    average = (sum/iteration)/10000
    print(average)