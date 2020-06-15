# 정수를 계속 입력받다가 100 이상의 수가 입력이 되면 마지막 입력된 수를 포함하여 합계와 평균을 출력하는 프로그램을 작성하시오.

# (평균은 반올림하여 소수 첫째자리까지 출력한다.)

a= input().strip().split()
i = 0
add_a = 0

while(int(a[i]) < 100):
    add_a = add_a + int(a[i])
    i = i+1

add_a = add_a + int(a[i])
print(add_a)
print(round(add_a/(i+1),1))
