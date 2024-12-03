def solution(numLog):
    answer = ''
    
    for i,n in enumerate(numLog):
        if len(numLog)-1 == len(answer):
            return answer;
        else:   
            case = numLog[i+1] - numLog[i];
        
            dict = {'w':1, 's':-1, 'd':10, 'a':-10}
        
            for i in dict:
                if dict[i] == case:
                    answer += i;    
        
    return answer;