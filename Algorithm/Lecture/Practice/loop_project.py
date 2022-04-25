# n = int(input("숫자를 입력해주세요 : "))
#
# '''
# 1번 ㅣ 1부터 N까지 홀수 출력하기
# '''

# for i in range(1, n + 1):
#     if i % 2 == 1:
#         print(i)
#
#
# '''
# 2번 | 1부터 N까지의 합 구하기
# '''
#
# print("2번 문제 시작")
#
# result = 0
#
# for i in range(1, n + 1):
#     result = result + i
#
# print(result)
#
#
# '''
# 3번 | N의 약수 출력하기
# '''
#
# print("3번 문제 시작")
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=' ')

# n = int(input("입력 : "))
#
# for i in range(5):
#     for j in range(i):
#         print("*", end = ' ')
#     print()

for i in range(5):
    for j in range(5 - i ):
        print("*", end=' ')
    print()