n = int(input('Enter number: '))
 
i=2
while i<=n/2:
    if n%i==0:
        print("number is not prime")
        break
    i+=1
else:
    print("prime number")    
