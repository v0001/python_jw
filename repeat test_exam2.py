# 0 이상의 정수들이 공백으로 구분되어 반복적으로 주어진다.

# 0이 입력되면 반복문을 멈추고 그 전까지 입력받은 수들에 대하여

# 홀수의 개수와 짝수의 개수를 출력하는 프로그램을 작성하시오.
i =0
a = input().strip().split(" ")
b =[]
cnt_odd = 0
cnt_even = 0

for i in range(0,len(a)):
    if a[i] == '0':
        break
    else:
        b.append(int(a[i]))
        continue

for i in range(0,len(b)):
    if b[i] % 2 == 0:
        cnt_even = cnt_even + 1
    else:
        cnt_odd = cnt_odd + 1

print('odd :',  cnt_odd)
print('even :',  cnt_even)