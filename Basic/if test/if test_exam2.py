# 정수를 입력받아 0 이면 "zero" 양수이면 "plus" 음수이면 "minus" 라고 출력하는 프로그램을 작성하시오.

a1 = int(input())

if a1 == 0:
    print('zero')
elif a1 > 0:
    print('plus')
else:
    print('minus')
