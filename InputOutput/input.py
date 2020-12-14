''' 공백을 기준으로 구분된 데이터를 입력 받을 때 '''
li = list(map(int, input().split()))

''' 공백을 기준으로 구분된 데이터를 입력 받을 때 (개수가 많지 않다면) '''
a, b, c = map(int, input().split())

''' 2차원 배열 데이터를 입력 받을 때 (N = 3, M = 4) '''
n = 3
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

''' 빠르게 입력 받기 '''
import sys
data = sys.stdin.readline().rstrip()
print(data)