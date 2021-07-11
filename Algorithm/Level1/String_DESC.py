def solution(s):
    answer = ''.join(reversed(sorted(s)))
    # join 함수 : 매게변수로 들어온 리스트를 문자열로 바꾸어서 반환함
    # ''의 의미 : 구분자
    # reversed 함수 안에 sort 함수를 이용하여서 내림차순으로 문자열을 정렬시킴

    return answer
