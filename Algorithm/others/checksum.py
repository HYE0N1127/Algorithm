l = []
mul = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
for i in range(0, 12):
    num = int(input())
    l.append(num * mul[i])
    result = sum(l) % 11
    result = 11 - result

if result > 9:
    result = result % 10
print(f'정답 : {result}')