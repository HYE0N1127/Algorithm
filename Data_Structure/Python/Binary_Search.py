def binary_search(array, elem, first, last):
    """
    :param array: 요소를 찾아야하는 배열
    :param elem: 찾으려는 요소
    :param first: 배열의 첫번째 인덱스
    :param last: 배열의 마지막 인덱스
    """
    if last < first:
        return False

    mid = (last + first) // 2

    if (array[mid] > elem):
        return binary_search(array, elem, first, mid - 1)

    elif (array[mid] < elem):
        return binary_search(array, elem, mid + 1, last)

    else:
        return True