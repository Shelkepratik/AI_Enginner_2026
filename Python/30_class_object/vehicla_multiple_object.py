class vehical:
    def __init__(self,color,top_speed,milage):#constructor
        self.color=color
        self.top_speed=top_speed
        self.milage=milage
    def display_info(self):
        print("color of the vehical:",self.color)
        print("Top speed of car is:",self.top_speed)
        print("mileage of car is:",self.milage)

#obj_name=class_name(argument)
print("========================")
tata=vehical("white",150,20)
tata.display_info()
print("========================")
honda=vehical("grey",180,60)
honda.display_info()
print("========================")
mahindra=vehical("blqck",160,17)
mahindra.display_info()
print("========================")

#access the indiviual attribute without method
print("The color of tata vehical is:",tata.color)
print("The color of tata vehical is:",honda.color)



#self is refernce object,self nothing but object
#self is replace the object
#init() method call ,after object is created