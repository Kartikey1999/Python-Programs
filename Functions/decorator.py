def outer(f):
    def inner():
        print("*"*16)
        f()
        print("*"*16)
    return inner
def oldf():
    print("Matrix Computers")
newf=outer(oldf)
newf()        