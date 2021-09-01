# Programmers Level 1 - 짝수와 홀수

def solution(num):
    odd = 'Odd'
    even = 'Even'

    if num % 2 == 1:
        return odd
    elif num % 2 == 0:
        return even
