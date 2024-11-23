def solution(code):
    answer = ''
    mode = 0
    
    for i, c in enumerate(code):
        
        if mode == 0:
            if c != '1':
                if i % 2 == 0:
                    answer += c
                else:
                    continue
            else:
                mode = 1
                continue
            
        if mode == 1:
            if c != '1':
                if i % 2 == 1:
                    answer += c
                else:
                    continue
            else:
                mode = 0     
                continue
        
    answer = 'EMPTY' if len(answer) == 0 else answer
    return answer