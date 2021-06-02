n=int(input("enter: "))
i=0
while i<=n:
    j=0
    while j<=i:
        print(chr(65+j),end='')
        j+=1
    print()
    i+=1    