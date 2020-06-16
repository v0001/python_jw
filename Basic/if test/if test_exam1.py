# 두 개의 정수를 입력받아 큰 수에서 작은 수를 뺀 차를 출력하는 프로그램을 작성하시오.



a1 = input().split()
a = int(a1[0])
b = int(a1[1])

if a>b:
    print(a-b)
else:
    print(b-a)


