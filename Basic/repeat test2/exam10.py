# 2부터 9까지의 수 중 2개를 입력받아 입력받은 수 사이의 구구단을 출력하는 프로그램을 작성하시오.
# 단 반드시 먼저 입력된 수의 구구단부터 아래의 형식에 맞게 출력하여야 한다.
# 구구단 사이의 공백은 3칸이다.

a = input().strip().split(' ')
first = int(a[0])
last = int(a[1])

total = 0
cnt = 0

if first < last:
    for i in range(1,10,1):
        for j in range(first,last+1,1):
            print(f'{j} * {i} = {i*j:2}  ', end=" ")
        print()

else:
    for i in range(1,10,1):
        for j in range(first,last-1,-1):
            print(f'{j} * {i} = {i*j:2}  ', end=" ")
        print()