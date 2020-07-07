# 10개의 정수를 입력받아 입력받은 수들 중 짝수의 개수와 홀수의 개수를 각각 구하여 출력하는 프로그램을 작성하시오.

a = input().strip().split(' ')
cnt_odd = int()
cnt_even = int()

for i in range(0,10,1):
    if int(a[i])%2==0:
        cnt_even += 1

    else:
        cnt_odd += 1

print("even :",cnt_even)
print("odd :",cnt_odd)    
