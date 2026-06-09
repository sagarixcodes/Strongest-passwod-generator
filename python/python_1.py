class Employee :
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
        print("Employee is successfully registered.")

    def Show_Details(self):
        print(f"Employee is an {self.role} working in {self.department} department on a salary of Rs.{self.salary} per month.")


class Engineer(Employee):
    def __init__(self,name,age,role,department,salary):
        self.name = name
        self.age = age

        super().__init__(role,department,salary)
        print(f"Mr.{self.name} of {self.age} years of age is an Engineer working in {self.department} department on a salary of Rs.{self.salary} per month.")
        

e1 = Employee("Civil Engineer","Constructional Development","50,000")
e1.Show_Details()
e2 = Engineer("Raghav Sharma","24","Civil Engineer","Constructional Development","50,000")