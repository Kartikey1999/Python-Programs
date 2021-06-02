fp=open("/var/www/learnPython/e.txt","w")
lst=["matrix\n","computer\n","education\n"]
fp.writelines(lst)
fp.close()