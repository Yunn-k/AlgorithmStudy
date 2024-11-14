def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    return answer
# 처음엔 my_string에서 교체구간만큼의 문자열을 구한 다음에 replace로 바꿔치기 했는데, 같은 문자열이 여러개 나올 경우 원하는 구간을 교체하지 못한다는 점에서 문제가 됨!