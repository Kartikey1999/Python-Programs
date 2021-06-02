fp=open("a.txt","r")
while True:
    s1=fp.readline()
    if s1:
        print(s1,end='')
    else:
        break
fp.close()    
