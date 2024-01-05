#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Representation of the Rectangle"""
    number_of_instances = 0
    '''number of active instances'''
    print_symbol = '#'
    '''symbol used to print the Rectangle'''

    def __init__(self, width=0, height=0):
        """initilationg of the rectangle with the height and width"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting width value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting height value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + (self.__height * 2)

    def __str__(self):
        """return a Rectangle in shape of hashtag #"""
        if self.__width == 0 or self.__height == 0:
            return ''
        string = ''
        for j in range(self.__height):
            string += self.__width * str(self.print_symbol) + '\n'
        return string[:-1]

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return "Rectangle("+str(self.__width)+", "+str(self.__height)+")"

    def __del__(self):
        """priting a message when and for every deletes of the rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method which compares the calculated area of rect_1 and rect_2"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
