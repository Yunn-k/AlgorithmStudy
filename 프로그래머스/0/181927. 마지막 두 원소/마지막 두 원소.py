def solution(num_list):
    answer = []
    
    the_last = num_list[len(num_list)-1];
    before_last = num_list[len(num_list)-2];
    
    if(the_last > before_last):
        # return num_list.append(the_last - before_last) #append메서드는 요소를 추가하고 반환이 none이므로 이렇게 한번에 리턴하면 안됨
        num_list.append(the_last - before_last)
    else:
        num_list.append(the_last * 2)

    return num_list;