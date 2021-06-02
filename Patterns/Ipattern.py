n=int(input("Enter:"))
mid=(n+1)//2
i=1
while i<=n:
    j=1
    while j<=n:
        if i==1 or j==mid or  i==n:
            print("*",end='')
        else:
            print(' ',end='')
        j+=1
    print()
    i+=1    