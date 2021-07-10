import datetime as dt


def solution(a, b):
    answer = ''

    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    answer = day[dt.datetime(2016, a, b).weekday()]
    # DateTime 라이브러리 사용

    return answer