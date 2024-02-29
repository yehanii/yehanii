ar_1=set(map(int,input('숫자를 입력하세요(,로 구분)').split(',')))

ar_2=set([4,5,6,7,8,24])

from random import *
ar_com=[]
for i in range(6):
    rd=randint(1,10)
    while rd in ar_com:
        rd=randint(1,10)
    ar_com.append(rd)
print(ar_com)
ar_2=set(ar_com)

ar= ar_1 & ar_2

print(ar)
print('맞은개수 : ',len(ar))

print(6-len(ar))