class lab_1():
    def Do2ndnum(self,N,b):
        while N > 0:
            b=str(N%2)+b
            N=N // 2
        return b
    def getResult(self,array,result):
        for val in array:
            if val == '1':
                result+=1
        print("Кол-во единиц:"+str(result))

obj=lab_1()
N=int(input())
b=''
result=0
array=list(obj.Do2ndnum(N,b))
print(str(array))
obj.getResult(array,result)
