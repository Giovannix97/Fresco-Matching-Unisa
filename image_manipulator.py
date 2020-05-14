import logging
import cv2
import traceback
from matplotlib import pyplot as plt



def get_image_size(opened_image):
    """
    Get original size of the image.

    :param opened_image:
    :return: A list of two values: height and width.
    """
    height, width, color_levels = opened_image.shape
    size = []
    size.append(height)
    size.append(width)
    return size


def get_image_height(opened_image):
    return opened_image.shape[0]


def get_image_width(opened_image):
    return opened_image.shape[1]


def get_image_color_levels(opened_image):
    return opened_image[2]




def rotate_image(image, angle, center = None, scale = 1.0):
    """
    Rotate and image using grades.

    :param image:
    :param angle: int value that represents grades.
    :param center:
    :param scale: Scaling factor. If not specified the image will not be scaled.
    :return: A rotated image.
    """
    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    # Perform the rotation
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated


def show_colors_histogram(colored_opened_image):
    """
    Show the color histogram for the specified image

    :param colored_opened_image:
    :return:
    """
    color = ('b', 'g', 'r')

    for i, col in enumerate(color):
        histr = cv2.calcHist([colored_opened_image], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()

def print_pixels_values(opened_image):
    try:
        print(opened_image)
    except(Exception):
        logging.error("Are you sure this image is a numpy array?")
        traceback.print_exc()



def get_percentage_of_black_pixels(opened_image):
    # TODO
    # This method must be implemented
    pass

    #return calculate_percentage(black_pixels_count, pixel_count + black_pixels_count)


def get_percentage_of_white_pixels(opened_image):
    # TODO
    # This method must be implemented
    pass

    # return calculate_percentage(white_pixels_count, pixel_count + white_pixels_count)
