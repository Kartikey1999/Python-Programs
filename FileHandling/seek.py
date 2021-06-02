fp=open("b.txt","r+")
fp.seek(2,0)
fp.write("tr")
fp.close()