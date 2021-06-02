n=int(input("enter a number"))

term=1
cnt=1
sign=1

while cnt<=n:
    term=2*cnt-1
    sign=-sign

    print(term*sign)
    
    cnt+=1