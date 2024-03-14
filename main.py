from algorithm_lehmera import generate_pseudo_random_numbers
from algorithm_vonneumanna import von_neumann


x0 = 2
a = 7
m = 11
n = 10
pseudo_random_numbers = generate_pseudo_random_numbers(x0, a, m, n)
print("Wygenerowane liczby pseudolosowe lehmer:", pseudo_random_numbers)

seed = 1211
iteration = 100
von_neumann(seed, iteration)
