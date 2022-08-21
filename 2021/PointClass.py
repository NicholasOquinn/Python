""" OOP Lab 2 - Question 2 - Nicholas O'Quinn

First Create Point Class

Attributes: X Coordinate and Y Coordinate """

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    def __str__(self):
        return
    f"X = {self.X}, Y = {self.Y}"


"""Create second class which is Rectangle Class

Attributes: X,Y Coordinate(of bottom left corner), the Height, and the Width"""

class Rectangle:
    def __init__(self, Btm_Lft_Crn, height, width):
        self.Btm_Lft_Crn = Btm_Lft_Crn
        self.height = height
        self.width = width

    # Method to retrieve height of rectangle
    def getHeight(self):
        return self.height

    # Method to retrieve width of function
    def getWidth(self):
        return self.width

    # method to return contents of object as string
    def __str__(self):
        return f"Bottom Left Corner: {self.Btm_Lft_Crn}, Height: {self.Height}, Width: {self.Width}"

    # method to calculate area of a rectangle
    def area(self):
        return self.width * self.height

    # method to find the perimeter of a rectangle
    def perimeter(self):
        return 2 * self.width + 2 * self.height

# create or instantiate the rectangle
Mybox = Rectangle(Point(1, 2), 3, 4)

p = Mybox.perimeter()
a = Mybox.area()






