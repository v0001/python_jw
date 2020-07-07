# 정수를 입력받아 다음과 같이 순서쌍을 출력하는 프로그램을 작성하시오.

 

# * 주의 

#  ')'와 '('사이에 공백이 1칸 있다.
# (1,_1) 처럼 출력한다 : '_'는 공백

a = int(input())

for i in range(1,a+1,1):
    for j in range(1,a+1,1):
        print(f'{i, j}', end = " ")
    print()