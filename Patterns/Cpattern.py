n=int(input("enter"))

i=1
while i<=n:
    j=1
    while j<=n:
        if i==1 or i==n or  j==1:
            print("*",end='')
        else:
            print(' ',end='')
        j+=1
    print()
    i+=1    