from functools import reduce
import random

print('Sum in numbers from 1 to 59')
numbers=range(1, 61)
sum = reduce(lambda x, y: x+y, numbers)
print(sum)

print('Max in numbers from 1 to 59')
max = reduce(lambda x, y: x if x > y else y, numbers)
print(max)

print('Min in numbers from 1 to 59')
min = reduce(lambda x, y: x if x < y else y, numbers)
print(min)

print("Generate 60 numbers ramdomly")
random_numbers = [random.randint(1, 61) for _ in range(6)]
print(random_numbers)

