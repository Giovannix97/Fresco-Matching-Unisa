from SizeImg import *
import cv2
from matplotlib import pyplot as plt
from Point import *
from BGR import *
from utils import calculate_percentage

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
        self.height = self.get_image_height()
        self.width = self.get_image_width()


    def get_opencv_image(self):
        """
        Get the real image opened with Open-CV library.
        :return: numpy array that represents an image.
        """
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


    def get_pixel_color_numpy(self, position=Point()):
        """
        Get the numpy array that represents the color of the pixel.
        :param position:
        :return: numpy array that represents the BGR values.
        """
        return self.opencv_image[position.get_x(), position.get_y()]


    def get_pixel_color_BGR(self, position=Point()):
        """
        Get a BGR object instead of a numpy array.

        :param position:
        :return: BGR object
        """
        np_array = self.opencv_image[position.get_x(), position.get_y()]
        return BGR.from_opencv_pixel_to_BGR_object(np_array)


    def change_pixel_color(self, position=Point(), bgr=BGR()):
        """
        Change the color of the specified pixel in a image.

        :param position: Point object that contains the coordinates: x and y.
        :param bgr: BGR object with the 3 colors.
        :return:
        """
        np_array = BGR.from_BGR_object_to_opencv_pixel(bgr)
        self.opencv_image[position.get_x(), position.get_y()] = np_array


    def get_neighbors_pixel_color(self, position=Point()):
        """
        Get all the BGR values of the neighbors.
        Let's consider a 3x3 matrix in which the chosen pixel is at the center. This method
        scan all the 8 pixel that surround the considered one.

        :param position:
        :return: a list of 8 numpy arrays. Each array represents tre BGR component of a neighbor.
        """

        x = position.get_x()
        y = position.get_y()

        assert x > 1 and y > 1, "X and Y must be greater or equal than 1!"

        if(x >= self.height - 1) or ( y >= self.width - 1):
            raise Exception("Please specify a lower value for x or y. It can't be greater than the maximum value of rows/columns.")

        pixels_colors_values = []
        for row in range(x-1, x+2):
            for column in range(y-1, y+2):
                if(row == x) and (column == y):
                    pass
                else:
                    pixels_colors_values.append(self.opencv_image[row,column])


        return pixels_colors_values


    def get_percentage_of_black_neighbors(self, position=Point()):
        """
        Get the percentage of black pixels that surround a pixel.
        Think it as a 3x3 matrix in which the pixel is at the centre.

        :param position: x and y coordinates of the central pixel.
        :return: A percentage that indicates the amount of black in the image.
        """

        # Get all neighbors BGR values
        neighbors_color_values = self.get_neighbors_pixel_color(position)
        black_pixels_count = 0


        for row in neighbors_color_values:
            blue, green, red = row
            if(blue == 0 and green == 0 and red == 0):
                black_pixels_count += 1

        return calculate_percentage(black_pixels_count,8)


    def get_blue_neighbors_pixel_values(self, position=Point()):
        """
        Select just the blue values of a numpy array.

        :param position:
        :return: a new numpy array of 8 values. Each value represent the blue component of BGR.
        """
        list_of_neighbors_pixels = self.get_neighbors_pixel_color(position)
        numpy_array = np.array(list_of_neighbors_pixels)
        return numpy_array[:,0]


    def get_green_neighbors_pixel_values(self, position=Point()):
        """
        Select just the green values of a numpy array.

        :param position:
        :return: a new numpy array of 8 values. Each value represent the green component of BGR.
        """
        list_of_neighbors_pixels = self.get_neighbors_pixel_color(position)
        numpy_array = np.array(list_of_neighbors_pixels)
        return numpy_array[:,1]


    def get_red_neighbors_pixel_values(self, position=Point()):
        """
        Select just the red values of a numpy array.

        :param position:
        :return: a new numpy array of 8 values. Each value represent red component of BGR.
        """
        list_of_neighbors_pixels = self.get_neighbors_pixel_color(position)
        numpy_array = np.array(list_of_neighbors_pixels)
        return numpy_array[:,2]


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



