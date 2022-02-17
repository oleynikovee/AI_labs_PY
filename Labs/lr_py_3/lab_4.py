import lab_4_lib
class Gonna:
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
    obj=lab_4_lib.ValueInt()
    print("Answer:"+str(obj.validation(array,type)))
