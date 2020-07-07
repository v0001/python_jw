# 자연수 n을 입력받고 1부터 홀수를 차례대로 더해나가면서 합이 n 이상이면 그 때까지 더해진 홀수의 개수와 그 합을 출력하는 프로그램을 작성하시오.

a = int(input())
count = 0
total = 0
i = 1

while(total<a):
    if(i%2==1):
        count = count +1
        total = total +i
        i = i+1
    else:
        i = i+1
        

print(f'{count} {total}')