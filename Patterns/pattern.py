n=5
k=5

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=' ')
    print()

for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print("*",end=' ')
    print()

    
