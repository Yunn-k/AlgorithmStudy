a = int(input())

print(f"{a} is {'even' if a%2 == 0 else 'odd'}")
#print문 내에 삼항연산자 처리 가능. 단 변경값은 {변수}로 묶어줌