# 1~12사이의 정수를 입력받아 평년의 경우 입력받은 월을 입력받아 평년의 경우 해당 월의 날수를 출력하는 프로그램을 작성하시오.
# 평년의 경우 1월부터 12월까지 일수는 각각 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31일이다.

a1 = int(input())

if a1 == 1 or a1 == 3 or a1 == 5 or a1 == 7 or a1 == 8 or a1 == 10 or a1 == 12:
    print('31')
elif a1 == 2:
    print('28')
else:
    print('30')