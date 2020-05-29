from SizeImg import *
import cv2
from matplotlib import pyplot as plt

class Image:
    """
    A wrapper to Open-CV image. The class contains some utils methods that will be applied on the cv2 image.

    ...

    Attributes
    ----------
    opencv_image: numpy.ndarray
            Numpy array that represents an image in Open-CV library.


    """
    def __init__(self,opencv_image):
        self.opencv_image = opencv_image


    def get_opencv_image(self):
        return self.opencv_image


    def get_image_size(self):
        """
        Get original size of the image.

        :param Open_Cv image:
        :return: A list of two values: height and width.
        """
        height, width, color_levels = self.opencv_image.shape
        return Size(height,width)


    def get_image_height(self):
        return self.opencv_image.shape[0]


    def get_image_width(self):
        return self.opencv_image.shape[1]


    def get_image_colors_levels(self):
        return self.opencv_image.shape[2]


    def show_colors_histogram(self):
        """
        Show the color histogram for the specified image

        :param:
        :return:
        """
        color = ('b', 'g', 'r')

        for i, col in enumerate(color):
            histr = cv2.calcHist([self.opencv_image], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
        plt.show()



