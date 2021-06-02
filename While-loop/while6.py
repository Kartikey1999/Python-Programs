n=int(input("enter a number"))

term=9
cnt=1

while cnt<=n:
    print(term, end=" ")
    term=term*10+9
    cnt+=1