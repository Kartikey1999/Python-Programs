class Employee:
    no_of_leaves=8
    
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printdetails(self):
        return f"Name is {self.name}. salary is {self.salary} and role is {self.role}"

harry=Employee("Harry",455,"Instructor")
# rohan=Employee()

# harry.name="harry"
# harry.salary=455
# harry.role="instructor"
# rohan.name="harry"
# rohan.salary=455
# rohan.role="student"

print(harry.salary)
