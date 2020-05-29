import numpy as np

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

    @staticmethod
    def from_opencv_pixel_to_BGR_object(cv2_img_pixel):
        """
        Method to convert an Open-CV object in a simple BGR object.

        :param cv2_img_pixel: Open_cv pixel in the form of numpy array [b,g,r].
        :return: A BGR object.
        """

        # Get the values ...
        blue = cv2_img_pixel[0]
        green = cv2_img_pixel[1]
        red = cv2_img_pixel[2]

        # and create an object with them.
        return BGR(blue, green, red)

    @staticmethod
    def from_BGR_object_to_opencv_pixel(bgr_object):
        """
        Method to convert a BGR object in an Open-CV object.

        :param bgr_object: A BGR object.
        :return: A numpy array that represents the BGR component.
        """

        # Get the values ...
        blue = bgr_object.get_blue()
        green = bgr_object.get_green()
        red = bgr_object.get_red()

        # and create a numpy array
        return np.array([blue, green, red])







