class Time:
    def __init__(self,hourse,minutes):
        self.hourse=hourse
        self.minutes=minutes
        
    def __str__(self):
        return "{} hours {}".format(self.hourse,self.minutes)

    def __add__(self,other):
        hourse=self.hourse+other.hourse
        minutes=self.minutes+other.minutes
        """convert extra minutes into hours"""
        hourse+=minutes//60
        minutes=minutes%60
        return Time(hourse,minutes)
    
    def __sub__(self, other):
        # Convert both durations into total minutes
        total1 = self.total_minutes()
        total2 = other.total_minutes()

        difference = total1 - total2

        # Convert the difference back into hours and minutes
        hourse = difference // 60
        minutes = difference % 60

        return Time(hourse, minutes)

    def total_minutes(self):
        return self.hourse * 60 + self.minutes


# Create two Time objects
t1 = Time(2, 45)
t2 = Time(1, 30)

print(t1)
print(t2)
print(t1 + t2)
print(t1 - t2)
print(t1.total_minutes())


