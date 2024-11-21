def solution(a, b):
    answer = 0
    
    temp_a = str(a)+str(b)
    temp_b = str(b)+str(a)
   
    if(int(temp_a) > int(temp_b)):
        answer = int(temp_a)
    else:
        answer = int(temp_b)
    
    return answer