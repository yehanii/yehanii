from random import *
ar_dict={}
ar_list=[]
ar_tuple=int()
str_char="name"

for i in range(10):
    rd=randint(1,10)
    ar_dict[i]=rd
    ar_list.append(rd)
    ar_tuple+=rd
    str_char+=str(rd)
    
print(ar_dict)
print(ar_list)
print(ar_tuple)
print(str_char)
