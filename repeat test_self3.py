# 한 개의 정수를 입력받아 양수(positive integer)인지 음수(negative number)인지 출력하는 작업을 반복하다가 0이 입력되면 종료하는 프로그램을 작성하시오.

# * 입출력예의 진한글씨는 출력값입니다.​ddd

a = 1

while(a!=0):
    a = int(input('number?\n'))
    if a>0:
        print('positive integer')
        continue
    elif a<0:
        print('negative number')
        continue
    else:
        break