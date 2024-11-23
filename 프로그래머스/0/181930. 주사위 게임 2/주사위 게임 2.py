def solution(a, b, c):
    answer = 0
    
    # 중복값을 지우는 set의 성질을 활용하여 체크
    check = len(set([a,b,c]))
    
    #기본값인 a+b+c를 변수로 처리
    answer = a + b + c
    
    if check == 1:
        return answer * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif check == 2:
        return answer * (a**2 + b**2 + c**2)
    else:
        return answer