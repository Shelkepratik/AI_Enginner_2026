class school:
    def __init__(self,school_name,city):
        self.school_name=school_name
        self.city=city
        
    def display_info(self):
        print("school name: ",self.school_name)
        print("school city: ",self.city)

school1=school("ABC school","pune")
school2=school("xyz school","mumbai")
print("Attribute call")
print(school1.school_name)
print(school1.city)
print("====================================")
school1.display_info()
print("===================================")
school2.display_info()