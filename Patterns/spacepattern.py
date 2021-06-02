n=int(input("enter: "))
i=1
while n>=i:
    print(" "*(n-i),end='')
    j=1
    while j<=2*i-1:
        print(j,end='')
        j+=1
    print()
    i+=1    