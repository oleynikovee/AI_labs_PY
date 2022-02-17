import cmath
import math
print("Input x")
x=int(input())
print("Input a")
a=int(input())
e=2.71828182846
if x<0:
    Y=cmath.sqrt(math.pow((math.pow(a,2)**(1./3.)-math.pow(x,2)**(1./3.)),3))
    print("Уравнение:"+str(Y))
if 0 <= x:
    Y=a+cmath.sqrt(math.pow(x,3)/(2*a-x))
    print("Уравнение:"+str(Y))
