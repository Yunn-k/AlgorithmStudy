def solution(a, b):
    answer = 0
    
    #max 사용으로 변경
    a, b = str(a), str(b)
    answer = max(int(a+b), int(b+a))
    
    return answer