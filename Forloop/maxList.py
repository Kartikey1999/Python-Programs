
l1=[]
n=eval(input("enter how many numbers: "))

for i in range(n):
   x=eval(input("enter element {}: ".format(i+1)))
   l1.append(x)
max=l1[0] 
for i in range(1,n):
   if l1[i]>max:
      max=l1[i]
print(max)      
