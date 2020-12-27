from itertools import combinations
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

''' 중복을 허용하지 않는 조합 '''
result = list(combinations(data, 2))
print(result)

''' 중복 조합 '''
result = list(combinations_with_replacement(data, 2))
print(result)