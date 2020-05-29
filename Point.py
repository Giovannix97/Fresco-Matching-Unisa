class Point:
    """
    A class to create a point made of two coordinates: x and y. It is used to represents a pixel inside an image.
    """

    def __init__(self,x=1,y=1):
        """
        Constructor
        
        :param x: default value is 1. This prevent from problems in the get_neighbors function
        :param y: default value is 1. This prevent from problems in the get_neighbors function
        """
        self.x = x
        self.y = y

    # Getters and setters
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self,x):
        self.x = x

    def set_y(self,y):
        self.y = y
