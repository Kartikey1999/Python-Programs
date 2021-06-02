data={}
n=int(input("Enter number of students: "))
for i in range(n):
    roll=int(input("Enter roll number of students {}: ".format(i+1)))
    marks=[]
    for j in range(3):
        m=int(input("Enter marks of student {}: ".format(j+1)))
        marks.append(m)
    data[roll]=marks
print(data)        