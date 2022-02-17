N=int(input())
array=list(range(0,N+10))
last=len(array)-1
buffer=array[0]
array[0]=array[last]
array[last]=buffer
print("Список: "+str(array))
