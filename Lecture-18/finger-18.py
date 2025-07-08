# Finger Exercises Lecture 18
# Name: Matias Ezequiel Petenatti
# Time Spent: 0:15

class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self._radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self._radius

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        return Circle(self._radius + c.get_radius())

    def __str__(self):
        """ A Circle's string representation is the radius """
        return str(self._radius)