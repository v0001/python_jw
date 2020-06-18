total = 0
avg = int()

num = input()
score = input().strip().split()

for i in range(0,len(score),1):
    total = total + int(score[i])

avg = total/len(score)
print("avg :","%.1f"%avg)
if avg >= 80:
    print("pass")
else: 
    print("fail")
    