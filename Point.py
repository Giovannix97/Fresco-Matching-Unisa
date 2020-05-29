class Point:
    """
    A class to create a point made of two coordinates: x and y. It is used to represents a pixel inside an image.
    """

    def __init__(self, x=1, y=1):
        """
        Constructor

        The default values are for a 3x3 mask. If you want to increase this mask, change them to higher numbers ( (2,2),(3,3) and so on ).

        :param x: default value is 1. This prevent from problems in the get_neighbors function
        :param y: default value is 1. This prevent from problems in the get_neighbors function
        """

        assert x >= 0 and y >= 0, "X and Y can't be negative!"

        self.x = x
        self.y = y

    # Getters and setters
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
