from math import prod
# math에 내장된 prod로 리스트의 곱셈값을 반환

def solution(num_list):
    return 1 if prod(num_list) < sum(num_list)**2 else 0