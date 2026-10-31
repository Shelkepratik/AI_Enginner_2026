print("start program")
class Fraction:
    def __init__(self,numerator,denominator):
        """ _ _init_ _:we can create an object"""
        self.numerator=numerator
        self.denominator=denominator


    def __str__(self):
        """_ _str_ _:when we print an object"""
        return "{}/{}".format(self.numerator,self.denominator)

    def __add__(self,other):
        new_num=(self.numerator*
                 other.denominator+
                 self.denominator*
                 other.numerator)
        new_den=(self.denominator*
                 other.denominator)
        return Fraction(new_num,new_den)

    def __mul__(self,other):
        new_num=(self.numerator*other.numerator)
        new_den=(self.denominator*other.denominator)
        return Fraction(new_num,new_den)

    def __truediv__(self,other):
            new_num=(self.numerator*other.denominator)
            new_den=(self.denominator*other.numerator)
            return Fraction(new_num,new_den)


Fraction1=Fraction(1,2)
Fraction2=Fraction(7,11)
print(Fraction1.numerator)
print(Fraction1.denominator)
print(Fraction2.numerator)
print(Fraction2.denominator)
print(Fraction1)
print(Fraction2)

print(Fraction1+Fraction2)
print(Fraction1*Fraction2)
print(Fraction1/Fraction2)



print("end program")