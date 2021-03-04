# 이진 탐색 (재귀)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    else:
        return binary_search(array, target, mid + 1, end)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(array, 4, 0, len(array) - 1))

# 이진 탐색 (반복)
def binary_search(array, target, start, end):
    while start <= end:

        mid = (start + end) // 2

        if mid == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(array, 4, 0, len(array) - 1))
