def solution(n, control):
    answer = 0
    
    dict = {'w':1, 's':-1, 'd': 10, 'a' : -10};
    
    #control에서 읽어온 값을 dict의 key와 일치시키면서 처리
    for c in control:
        n += dict[c]
    
    return n;