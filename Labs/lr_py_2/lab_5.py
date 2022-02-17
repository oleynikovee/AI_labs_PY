N=int(input())+6
result=1
if N>0:
    for i in range(1,N):
        result*=i
    print("Факториал равен:"+str(result))
