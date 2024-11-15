def solution(str1, str2):
    result = []

    for a, b in zip(str1, str2): #zip함수를 사용하여 각 요소를 튜플형태로 반환받음
        result.append(a)
        result.append(b)

    answer = ''.join(result)
    return answer