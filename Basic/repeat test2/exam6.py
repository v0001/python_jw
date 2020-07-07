# 두 개의 정수를 입력받아 두 정수 사이(두 정수를 포함)에 3의 배수이거나 5의 배수인 수들의 합과 평균을 출력하는 프로그램을 작성하시오.

# (평균은 반올림하여 소수 첫째자리까지 출력한다.)

a = input().strip().split(' ')
first = int()
last = int()
total = 0
cnt = 0

if int(a[0])<int(a[1]):
    first = int(a[0])
    last = int(a[1])
else:
    last = int(a[0])
    first = int(a[1])

for i in range(first, last+1, 1):
 
    if i%3==0 or i%5==0:
        total = total+ i
        cnt = cnt +1

    else:
        continue

print("sum :", total)
print("avg :", round(total/cnt,1))

