l1=[]
n=eval(input("enter: "))

for i in range(n):
    x=eval(input("enter element {}: ".format(i+1)))
    l1.append(x)

for i in range(len(l1)-1,-1,-1):
    print(l1[i])
    