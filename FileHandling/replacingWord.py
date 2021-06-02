fp1=open("d.txt","r")
fp2=open("/var/www/learnPython/e.txt","w")

s1=fp1.read()
s1=s1.replace("is","was")
fp2.write(s1)
fp1.close
fp2.close

