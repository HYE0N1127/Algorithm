num = int(input())
i = 2
result = []

if num == 1:
    print(1)
else :
    while num != 1:
        if num % i == 0:
            num = num / i
            result.append(i)
        else : i+=1

factor = set(result)
factor = list(factor)
i = 0
for j in factor:
    print(f'{factor[i]} ^ {result.count(j)}')
    i += 1