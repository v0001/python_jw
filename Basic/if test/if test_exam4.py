# 1번은 개, 2번은 고양이, 3번은 병아리로 정하고 번호를 입력하면 번호에 해당하는 동물을 영어로 출력하는 프로그램을 작성하시오.
# 해당 번호가 없으면 "I don't know."라고 출력한다.

# 개-dog

# 고양이-cat

# 병아리-chick​ 

a1 = input("Number? ").strip()

if a1 == '1':
    print('dog')
elif a1 == '2':
    print('cat')
elif a1 == '3':
    print('chick')
else:
    print("I don't know.")