
def mySum(n):
    if n==0:
        return 0
    else:
        return n%10+mySum(n//10)
n=int(input("enter"))
print(mySum(n))            