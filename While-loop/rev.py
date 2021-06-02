

n=int(input("enter"))
old=n
rev=0


while n:
    rev=rev*10+n%10
    n//=10

if old==rev:

    print("pallindrome")
else:
    print("not pallindrome")        