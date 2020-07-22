class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
 
rec_l = float(input("Length:  "))
rec_w = float(input("Width:  "))
 
rec_a = Rectangle(rec_l, rec_w)
 
print ("The Area is:  ", rec_a.area())

