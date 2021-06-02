def myMult(a, b):
    if a == 0 or b==0:
        return 0

    else:
        return a + myMult(a, b-1)


a,b = map(int,input("enter two num: ").split())
print(myMult(a,b))