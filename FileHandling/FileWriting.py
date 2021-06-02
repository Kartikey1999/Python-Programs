# f=open ("hello.txt","a")
# a=f.write('hello there by')
# print(a)
# f.close()

f=open ("hello.txt","r+")
# a=f.write('hello there by')
print(f.read())
f.write('thank you')