y=int(input("enter a year"))

if y%100==0 and y%400==0:
        print("leap year")

else:
    if y%4==0:
        print("leap year")
    else:
        print("no")

   