import random

ar=random.sample(range(1,46),6)
print(ar)
br=[]
cnt=0
print("로또 번호 입력!")

for x in range(6):
    br.append(int(input()))
print(br)

for i in range(6):
    for j in range(6):
        if ar[i]==br[j]:
            cnt+=1
print(cnt,"개")
if cnt==4:
    print("4개 맞춤! 3등입니다!\n애매한 행운을 가지고 계시군요!")
elif cnt==5:
    print("5개 맞춤! 2등입니다!\n아깝다! 하나만 더 하면 1등인데!")
elif cnt==6:
    print("6개 맞춤! 1등입니다!\n당신은 행운의 사나이!")
else:
    print("{}개 맞춤! 꽝이네요...\n심심한 위로를 전합니다...".format(cnt))