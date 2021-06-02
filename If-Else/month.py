

month=int(input("enter month number"))

if month in [1,3,5,7,9]:
    print("31 days")
elif month==2:
    print("28 days")
elif month in [2,4,6,8]:
    print("30 days")        


