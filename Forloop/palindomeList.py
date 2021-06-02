l1=[]

n=eval(input("enter: "))

for i in range(n):
    x=eval(input("enter elements {}: ".format(i+1)))
    l1.append(x)

l2=[]

for i in range(n-1,-1,-1):
    l2.append(l1[i])
if l1==l2:
    print("palindrome")
else:
    print("not ")    
