def solution(my_string, overwrite_string, s):
    list_m = list(my_string)
    list_o = list(overwrite_string)
    list_m[s:s+len(list_o)] = list_o
    answer = ''.join(list_m) #리스트의 문자들을 이어붙여 문자열로 만듦
    return answer
