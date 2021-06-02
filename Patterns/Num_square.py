'''First Half of the Pattern'''


n=int(input("enter: "))
i=n
while i>=1:
    
    j=n
    while j>=i:
        
        print(j,end='')
        j-=1

    k=1
    while k<=2*i-3:
        print(i,end='')
        k+=1

    l=i
    while l<=n:
        # if l==1:
        #     continue
        print(l,end='')
        l+=1    
    print()
    i-=1

'''Second Half of the Pattern'''    


i=2
while i<=n:
    
    j=n
    while j>=i:
        print(j,end='')
        j-=1

    k=1
    while k<=2*i-3:
        
        print(i,end='')
        k+=1

    l=i
    while l<=n:
        if l==1:
            continue
        print(l,end='')
        l+=1    
    print()
    i+=1            