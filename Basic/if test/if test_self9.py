# 3개의 정수를 입력받아 조건연산자를 이용하여 입력받은 수들 중 최소값을 출력하는 프로그램을 작성하시오.

a1 = input().split()
a = int(a1[0])
b = int(a1[1])
c = int(a1[2])

if a<b:
    if a<c:
        print(a)
    else:
        print(c)
else:
    if b<c:
        print(b)
    else:
        print(c)

