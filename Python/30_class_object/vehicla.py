class vehical:
    #constructor
    #self is refernce of the object
    def __init__(self):
        self.color="yellow" #Attribute1
        self.top_speed=150 #Attribute2
        self.milage=15 #Attribute3
    def diasplay_info(self):
        print("The color:",self.color)
        print("The top speed of vehical:",self.top_speed)
        print("The milage is:",self.milage)
#tata info
tata=vehical()
tata.diasplay_info()
print(tata.color)

print("____________________________________________________________________")
#hondai info
hondai=vehical()
hondai.diasplay_info()
