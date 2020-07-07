# 자연수 n을 입력받아서 n줄만큼 다음과 같이 출력하는 프로그램을 작성하시오.

a = int(input())
len = str(a)


for i in range(a,0,-1):
    result = "*"*(i*2-1)
    # print("{:*>i}".format())
    print(result.center(a*2-1))

