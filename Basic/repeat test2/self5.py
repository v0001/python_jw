# 10개의 정수를 입력받아 3의 배수의 개수와 5의 배수의 개수를 각각 출력하는 프로그램을 작성하시오. 


i =0
a = input().strip().split(" ")
cnt_three = 0
cnt_five = 0

for i in range(0, 10 ,1):
    if int(a[i])%3 == 0 and int(a[i])%5 != 0:
        cnt_three = cnt_three +1
        print(a[i],3)
    elif int(a[i])%5 == 0 and int(a[i])%3 != 0:
        cnt_five = cnt_five +1
        print(a[i],5)
    elif int(a[i])%3 == 0 and int(a[i])%5 == 0:
        cnt_three = cnt_three +1
        cnt_five = cnt_five +1
    else:
        continue

print("Multiples of 3 : ",cnt_three)
print("Multiples of 5 : ", cnt_five)