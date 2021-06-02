fp1=open("a.txt","r")
fp2=open("b.txt","r")
fp3=open("/var/www/learnPython/c.txt","w")
s1=fp1.read()
s2=fp2.read()

fp3.write(s1)
fp3.write(s2)