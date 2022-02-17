class lab_2():
    def getListNums(self,a,t,z,array):
        for i in range(z):
            if i==0:
                array[i]=a
            else:
                array[i]=a+(i*t)
        return array
    def result(self,array):
        result=1
        for val in array:
            result*=float(val)
        return result

a=float(input())
t=float(input())
z=int(input())
array=list(range(0,z))
obj=lab_2()
next=list(obj.getListNums(a,t,z,array))
print("Результат: "+str(obj.result(next)))
