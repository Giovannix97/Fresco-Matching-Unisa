from Point import *
from BGR import *


class Pixel:
    """
    A class to model a Pixel.
    A pixel is described by his position (x and y coordinates in the image), by his color (BGR model for Open-CV)
    and by an accuracy.
    """

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

    def set_position(self, position):
        """

        :param position: a Point object composed by two coordinates, x and y.
        :return:
        """
        self.position = position

    def set_BGR(self, BGR):
        """

        :param BGR: a BGR object composed of three colors: blue,green and red
        :return:
        """
        self.BGR = BGR

    def set_weight(self, weight):
        self.weight = weight


