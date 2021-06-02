n=int(input("enter: "))
mid=(n+1)//2
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==n or i==mid or (j==1 and i<mid):
            print("*",end='')
        else:
            print(" ",end='') 
    print()    
              