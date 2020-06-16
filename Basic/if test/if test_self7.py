# 영문 대문자를 입력받아 

# 'A'이면 “Excellent”, 

# 'B'이면 “Good”, 

# 'C'이면 “Usually”, 

# 'D'이면 “Effort”, 

# 'F'이면 “Failure”, 

# 그 외 문자이면 “error” 라고 출력하는 프로그램을 작성하시오.


a = input().strip().upper()

if a == 'A':
    print('Excellent')
elif a == 'B':
    print('Good')
elif a == 'C':
    print('Usually')
elif a == 'D':
    print('Effort')
elif a == 'F':
    print('Failure')
else:
    print('error')
