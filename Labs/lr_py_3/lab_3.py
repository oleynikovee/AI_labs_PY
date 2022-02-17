class progGeo():
    def getProgres(self,array,a,t,alim):
        while a > alim:
            array.append(a)
            a=a*t
        return array
    def getResultOfGeo(self,array,sum):
        for val in array:
            sum+=val
        return sum
print("Input a:")
a=float(input())
print("Input t:")
t=float(input())
print("Input alim:")
alim=float(input())
array=list()
sum=0
obj=progGeo()
sum=obj.getResultOfGeo(obj.getProgres(array,a,t,alim),sum)
print("Сума чисел до "+str(alim)+" равна:"+str(sum))
