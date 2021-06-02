# import os
# if os.path.exists("var/www/learnPython/b.txt"):
fp1=open("a.txt","r")
fp2=open("/var/www/learnPython/b.txt","w")
s1=fp1.read()
s1=s1.upper()
fp2.write(s1)
fp1.close()
fp2.close()