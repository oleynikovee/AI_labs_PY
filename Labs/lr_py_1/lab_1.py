import math
a=5
b=4
c=2
p=(a+b+c)/2
result=p*(p-a)*(p-b)*(p-c)
sqrt=math.sqrt(result)
print("Площадь треугольника при a="+str(a)+" b="+str(b)+" c="+str(c)+" равна S="+str(sqrt))
