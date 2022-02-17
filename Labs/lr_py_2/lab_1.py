x=float(input())
y=float(input())
if -3 <= x <= 3:
    if -1 <= y <= 2:
        if -2<=y<=0 and -1<=x<=1:
            print("Принадлежит")
        else:
            print("Не принадлежит")
else:
    print("Не принадлежит")
