n=int(input("enter: "))
mid=(n+1)//2
i=1
while i<=n:
    print(" "*(n-i),end='')
    j=1
    while j<=2*i-1:
        if j==1 or j==2*i-1 or i==mid:    
            print("*",end='')
        else:
            print(" ",end='')
        j+=1
    print()
    i+=1