def solution(num_list):
    answer = []
    
    last = num_list[-1];
    before_last = num_list[-2];
    
    return num_list + [last - before_last] if last > before_last else num_list + [last * 2];