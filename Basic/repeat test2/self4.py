# 100 이하의 정수를 입력받아서 입력받은 정수부터 100까지의 합을 출력하는 프로그램을 작성하시오.

a = int(input())
total = 0

while(a <= 100):
    total = total +a
    a = a+1

print(total)