def plus_one(x):
    return x + 1


a = [1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x + 1, a)))
