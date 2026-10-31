class Employee:

    company_name="TCS" #static variable

    def __init__(self,emp_name,dep):#instance variable
        self.emp_name=emp_name
        self.dep=dep

    def display_info(self):#instance method
        print("The Empoyee name:",self.emp_name)#access the instance variable
        print("empoyee deparment:",self.dep)
        print("Company name:",Employee.company_name)#access the static variable

emp1=Employee("pratik","IT")

emp1.display_info()
