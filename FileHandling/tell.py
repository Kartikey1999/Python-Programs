fp=open("b.txt","r+")
print("Current Position is", fp.tell()) #0
fp.seek(2,0)
print("Current Position is", fp.tell()) #2
fp.write("tr")
print("Current Position is", fp.tell()) #4

fp.close()