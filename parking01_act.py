a,b=map(int,input('입차시간(00:00): ').split(':'))
c,d=map(int,input('출차시간(00:00): ').split(":"))
time=(c*60+d)-(a*60+b)
print("총 주차 시간 {}분".format(time))
fee=time//10*500
print("총 주차 요금 {:,}원".format(fee))
