# 자연수 n을 입력받아 "출력 예"와 같이 공백으로 구분하여 출력하는 프로그램을 작성하시오.
# 주의! 숫자를 공백으로 구분하되 줄사이에 빈줄은 없다.


a = int(input())
len = str(a)
result = ""
b = 1

for i in range(1,a+1,):
    for j in range(1,i+1):
        if (j<10):
            result = result +str(j).ljust(2)
        # elif (j==10):
        #     result = result +" "+str(j).ljust(3)
        else:
            result = result +str(j).ljust(2) +" "

    print(result.strip().rjust(a+a-1))
    result = ""