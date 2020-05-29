import statistics
import os
import cv2



def is_int_number_even(number):
    if (number % 2) == 0:
        return True

    return False


def calculate_percentage(value, total):
    """
    A simple method to calculate percentage
    :param value:
    :param total:
    :return:
    """
    return (value * 100) / total


def calculate_int_average(values):
    """
    Get int average

    :param values: A list of n values
    :return: An int value that represents an average.
    """
    return int(statistics.mean(values))


def calculate_int_median(values):
    """
        Get int median

        :param values: A list of n values
        :return: An int value that represents the median value.
        """
    return int(statistics.median(values))


def get_img_path(image_name):
    """
    Get the path of the chosen fragment.

    :param image_name:
    :return: A string that represents the image path.
    """
    folder_path = os.getcwd()
    return folder_path + "\images\\fragments\\" + image_name


def get_folder_path():
    """
        Get the path of the folder in which are stored all the fragments

        :return: A string that represents the image path.
        """
    folder_path = os.getcwd()
    return folder_path + "\images\\fragments"


def verify_if_path_exists(path):
    """
    Verify if the image/folder exists.

    :param path:
    :return: True if the path exists.
    """
    return os.path.exists(path)



def save_image(image, filename="output_img.png"):
    """
    Save the specified image in the "fragments" folder.

    :param image: Image to save
    :param filename: A name for the image with the extension. If not specified the default is output_img.png
    :return:
    """
    folder_path = get_folder_path()
    os.chdir(folder_path)

    try:
        cv2.imwrite(filename, image)
        print("Image saved successfully!")
    except:
        print("Error while saving image!")

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