class Employee:
    emp_count = 0
    salary = 0

    def __init__(self, name, family, salary, dept):
        self.name = name
        self.family = family
        Employee.salary += salary
        self.dept = dept
        Employee.emp_count += 1

    def display_emp_count(self):
        print("\nTotal number of employees : ", Employee.emp_count)

    def avg_salary(self):
        avg_sal = Employee.salary / Employee.emp_count
        print("\nAverage salary of employees :", avg_sal)


#Derived class Full_time_Employee
class Full_time_employee(Employee):
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Displaying Employee name : " +self.name)

    def createObjects():
        enter = 'yes'
        while enter == 'yes' :
            name = input("Enter name of employee : ")
            family = input("Enter family : ")
            salary = int(input("Enter salary : "))
            Department = input("Enter department : ")
            e = Employee(name,family,salary,Department)
            enter = input("Do you want to enter employee details? yes/no : ")
            a = Full_time_employee('Deepika')
            a.display_emp_count()
            a.avg_salary()
            a.display()

Full_time_employee.createObjects()
