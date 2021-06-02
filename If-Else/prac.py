n=int(input("enter:"))

mid=(n+1)//2

for i in range(1,n+1):
    # print(" "*(n-i),end='')

    for j in range(1,n*2):
        if j== or j==n*2-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()            