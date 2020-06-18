# 0 이 입력될 때까지 정수를 계속 입력받아 3의 배수와 5의 배수를 제외한 수들의 개수를 출력하는 프로그램을 작성하시오.


i =0
a = input().strip().split(" ")
b =[]
cnt = 0

for i in range(0,len(a)):
    if int(a[i]) ==0:
        break
    else:
        b.append(int(a[i]))
        continue

for i in range(0, len(b),1):
    if int(b[i])%3 == 0 or int(b[i])%5 == 0:
        continue
    else:
        cnt = cnt +1

print(cnt)