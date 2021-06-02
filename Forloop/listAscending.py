l1=[]
n=eval(input("enter how many number: "))

for i in range(n):
    x=eval(input("enter element {} ".format(i+1)))
    l1.append(x)

prev=l1[0]
for i in range(1,n):
    if l1[i]<prev:
        print("list is not in asce")
        break
else:
    print("list is in asce")    


    
  


