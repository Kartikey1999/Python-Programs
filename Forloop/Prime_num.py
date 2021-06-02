n=int(input("enter"))    

for i in range(2,n//2+1):
    if n%i==0:
        print("not a prime number")

        break
else:
    print("prime number")    