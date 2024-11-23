def solution(a, d, included):
    answer = 0
    
    for i, b in enumerate(included):
        if(b == True):
            answer += (a + (i * d))
            
    return answer