# 100 이하의 두 개의 정수를 입력받아 작은 수부터 큰 수까지 차례대로 출력하는 프로그램을 작성하시오.

a = input().strip().split(' ')

first = int(a[0])
last = int(a[1])

if (first<last):
    for i in range(first, last+1,1):
        print(i)

else:
    for i in range(last, first+1,1):
        print(i)



