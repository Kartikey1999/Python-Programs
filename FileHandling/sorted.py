fp1=open("b.txt","r")
fp2=open("/var/www/learnPython/f.txt","w")

s1=fp1.read()
s1 = sorted(s1)
fp2.write(s1)
fp1.close
fp2.close