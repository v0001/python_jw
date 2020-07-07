# 행과 열의 수를 입력받아 다음과 같이 출력하는 프로그램을 작성하시오.

a = input().strip().split(' ')
vertical = int(a[0])
horixont = int(a[1])
print(vertical,horixont)

for i in range(1,vertical+1,1):
    
    for j in range(1,horixont+1,1):
        print(i*j, end=" ")
    print()
    
