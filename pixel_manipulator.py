import logging
import numpy as np
from image_manipulator import get_image_size
from utils import calculate_percentage


logging.basicConfig(level=logging.disable())


def get_pixel_color(image, x, y):
    """
    Return BGR specified pixel color value

    :param image:
    :param x:
    :param y:
    :return: A BGR value associated to the pixel.
    """
    if(x < 0) or (y < 0):
        raise Exception("X or Y value cannot be negative!")
    return image[x, y]


def change_pixel_color_and_return_image_BGR(image, x, y, blue_value, green_value, red_value):
    """
    Manipulate BGR value of a specified pixel and returns a new image

    N.B. OpenCv uses BGR instead of RGB.

    :param image:
    :param x:
    :param y:
    :param blue_value: int value from 0 to 255
    :param green_value: int value from 0 to 255
    :param red_value: int value from 0 to 255
    :return: A new manipulated image.


    """
    image[x, y] = [blue_value, green_value, red_value]
    return image


def get_neighbors_pixels_colors(image, x, y):
    """
    Return a list that contains all the neighbors of the specified pixel.

    Let's consider a 3x3 matrix, in which the considered pixel is located at the center.
    Starting from the top left corner and sliding each single row, all the BGR are stored
    in the returned list.

    :param image:
    :param x:
    :param y:
    :return: A list of 8 BGR values
    """
    # x and y value can't be negatives.
    if(x < 1) or (y < 1):
        raise Exception("X and Y must be greater or equal than 1!")

    # Values of row/column can't go further the image.
    image_size = get_image_size(image)
    if(x >= image_size[0] - 1) or (y >= image_size[1] - 1):
        raise Exception("Please specify a lower value for x or y. It can't be equal to the maximum value of rows/columns.")

    pixels_colors_values_list = []
    for row in range(x - 1, x + 2):
        for column in range(y - 1, y + 2):
            if(row == x) and (column == y):
                pass
            else:
                pixels_colors_values_list.append(image[row, column])

    return pixels_colors_values_list


def get_percentage_of_black_neighbors(image, x, y):
    """
    Get the percentage of black pixels that surround a pixel.

    :param image:
    :param x:
    :param y:
    :return: A percentage that indicates the amount of black in the image.
    """

    # Get all neighbors BGR values
    neighbors_values = get_neighbors_pixels_colors(image,x,y)
    logging.info(neighbors_values)

    black_pixels_count = 0

    for row in neighbors_values:
        blue,green,red = row
        if(blue == 0) and (green == 0) and (red == 0):
            # The pixel is black
            black_pixels_count += 1

    return calculate_percentage(black_pixels_count,8)


def get_blue_neighbors_pixel_values(image, x, y):
    list_of_neighbors_pixels = get_neighbors_pixels_colors(image,x,y)
    numpy_array = np.array(list_of_neighbors_pixels)

    return numpy_array[:,0]


def get_green_neighbors_pixel_values(image, x, y):
    list_of_neighbors_pixels = get_neighbors_pixels_colors(image, x, y)
    numpy_array = np.array(list_of_neighbors_pixels)

    return numpy_array[:,1]


def get_red_neighbors_pixel_values(image, x, y):
    list_of_neighbors_pixels = get_neighbors_pixels_colors(image, x, y)
    numpy_array = np.array(list_of_neighbors_pixels)

    return numpy_array[:,2]