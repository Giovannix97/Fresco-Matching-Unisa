class BGR:
    """
    A class to model a BGR color used in Open-CV

    ...

    Attributes
    ----------
    blue : int
        int value that represents the blue component. The value is in the interval between 0 and 255
    green : int
        int value that represents the green component. The value is in the interval between 0 and 255
    red : int
        int value that represents the red component. The value is in the interval between 0 and 255


    """
    def __init__(self, blue=0, green=0, red=0):
        """ Constructor: if not specified, the BGR color will be black (000) """
        assert blue <=255 and green <= 255 and red <=255 and blue >= 0 and green >= 0 and red >= 0
        self.blue = blue
        self.green = green
        self.red = red

    # Getters and setters
    def get_blue(self):
        return self.blue

    def get_green(self):
        return self.green

    def get_red(self):
        return self.red

    def set_blue(self,blue):
        self.blue = blue

    def set_green(self,green):
        self.green = green

    def set_red(self,red):
        self.red = red









