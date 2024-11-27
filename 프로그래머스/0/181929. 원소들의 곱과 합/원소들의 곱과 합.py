def solution(num_list):
    mul = 1 #곱셈은 0으로 초기화하면 안됨
    sum_ = 0
    for n in num_list:
        mul *= n
        sum_ += n

    return 1 if mul < sum_**2 else 0