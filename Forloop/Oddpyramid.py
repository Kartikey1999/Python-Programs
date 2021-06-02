n=int(input("enter: "))

for i in range(1,n+1):
    print(" "*(n-i),"*"*(2*i-1) ,end='')
    
    # for j in range(1,2*i):
    #     print(j,end='')
    print()            