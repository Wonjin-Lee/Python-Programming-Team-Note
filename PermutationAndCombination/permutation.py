from itertools import permutations
from itertools import product

data = ['A', 'B', 'C']

''' 중복을 허용하지 않는 순열 '''
result = list(permutations(data, 3))
print(result)

''' 중복 순열 '''
result = list(product(data, repeat=2))
print(result)