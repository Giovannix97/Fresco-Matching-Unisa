from Point import *
from BGR import *


class Pixel:
    def __init__(self, position=Point(), BGR=BGR(), weight=1):
        """

        :param position: Position of the pixel expressed as x and y coordinates
        :param BGR: Blue, green and red values of the pixel.
        :param weight: Accuracy of the pixel between 0 and 1. It indicates the percentage of which the pixel is similar to the real one.

        """
        self.position = position
        self.BGR = BGR
        self.weight = weight

    # Getters and setters
    def get_position(self):
        """

        :return: a Point object.
        """
        return self.position

    def get_BGR(self):
        """

        :return: a BGR object.
        """
        return self.BGR

    def get_weight(self):
        return self.weight

    def set_position(self,position):
        """

        :param position: a Point object composed by two coordinates, x and y.
        :return:
        """
        self.position = position

    def set_BGR(self,BGR):
        """

        :param BGR: a BGR object composed of three colors: blue,green and red
        :return:
        """
        self.BGR = BGR

    def set_weight(self,weight):
        self.weight = weight


    def is_black(self):
        """
        Check if the current pixel is black.

        :return: True if the pixel is black.
        """
        blue = self.get_BGR().get_blue()
        green = self.get_BGR().get_green()
        red = self.get_BGR().get_red()

        if blue == 0 and green == 0 and red == 0:
            return True
        return False