def solution(a, b, c):
    answer = 0
    
    # 중복값을 지우는 set의 성질을 활용하여 체크
    check = len(set([a,b,c]))
    
    if check == 1:
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    else:
        answer = (a + b + c) * (a**2 + b**2 + c**2) if check == 2 else (a + b + c)
    
    return answer