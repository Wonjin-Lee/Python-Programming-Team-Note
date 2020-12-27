''' sorted with key '''
array = [('Lee', 35), ('Kim', 50), ('Choi', 45)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)