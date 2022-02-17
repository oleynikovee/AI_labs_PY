import lab_4_lib
class SumOfNumAndIndex():
    def vali(self,array,type):
        if lab_4_lib.ValueInt().validation(array,type):
            print("Before:"+str(array))
            counter=0
            buffer=0
            for val in array:
                buffer=int(val)+counter
                array[counter]=buffer
                counter+=1
            print("After:"+str(array))

print("Input type of sort:")
print("Whre 0 is ascending nad 1 is descending:")
type=int(input())
print("Input size of array where size will be N+5")
N=int(input())
print("Input")
array=[]
for num in range(N+5):
    print("Input item in array["+str(num)+"]:")
    x=input()
    array.append(x)
obj=SumOfNumAndIndex()
obj.vali(array,type)
