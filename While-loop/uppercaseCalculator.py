def string_test(s):
    d={"Upper":0,"lower":0}

    for c in s:
        if c.isupper():
            d["Upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("original string",s)                
    print("Upper string",d["Upper"])                
    print("Lower string",d["lower"])
print(string_test("Hello Kartikey"))                    




