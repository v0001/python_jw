# 정수를 입력받아서 1부터 입력받은 정수까지의 5의 배수의 합을 구하여 출력하는 프로그램을 작성하시오.

a = int(input())
total = int()

for i in range(1,a+1,1):
    if i%5 ==0:
        total =total + i
    else:
        continue

print(total)