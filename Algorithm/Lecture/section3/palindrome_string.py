import sys
sys.stdin = open("input/palindrome_string/input.txt", "rt")

n = int(input())

for i in range(0, n):
    word = input()
    word = word.upper()
    length = len(word)

    for j in range(length // 2):
        if word[j] != word[-1-j]:
            print(f'#{i + 1} NO')
            break
    else:
        print(f'#{i + 1} YES')

