n=int(input("enter"))
mid=(n+1)//2
i=1
while i<=n:
    j=1
    while j<=n:
        if i==1 or i==n or i== mid or j==1 or j==n:
            print("*",end='')
        else:
            print(' ',end='')
        j+=1
    print()
    i+=1        
