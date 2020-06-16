# 0 부터 100 까지의 점수를 계속 입력받다가 범위를 벗어나는 수가 입력되면 그 이전까지 입력된 자료의 합계와 평균을 출력하는 프로그램을 작성하시오.

# (평균은 반올림하여 소수 첫째자리까지 출력한다.)


i =0
a = input().strip().split(" ")
b =[]
total = 0

for i in range(0,len(a)):
    if int(a[i]) >100 or int(a[i]) < 0:
        break
    else:
        b.append(int(a[i]))
        continue

for i in range(0,len(b)):
    total = total + b[i]

print('sum :', total)
print('avg :', round(total/len(b),1))