n=int(input("enter week number"))

#DICTIONARY METHOD


dict={1:"sun",2:"mon",3:"tues"}

if n>=1 and n<=7:
    print(dict[n])
else:
    print("invalid")  

#LIST METHOD


list=['sun','mon','tues','wed']

if n>=1 and n<=7:
    print(list[n-1])
else:
    print("invalid")    


