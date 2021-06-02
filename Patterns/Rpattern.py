n=int(input("enter: "))
mid=(n+1)//2
for i in range(1,n+1):
    for j in range(1,n//2+3):
        if i==1 or j==1 or i==mid or (j==n//2+2 and i<=mid) or (j==i-2 and i>=mid):
            print("*",end='')
        else:
            print(" ",end='')
    print()  