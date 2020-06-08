from utils import *
from Image import *
from excelFile import *


IMG_NAME = "frag_66"
IMG_EXTENSION = ".png"
IMAGE_NAME = IMG_NAME + IMG_EXTENSION

MINIMUM_WEIGHT = 0
MAXIMUM_WEIGHT = 10
MEDIUM_WEIGHT = 5


def save_image(image, filename="output_img.png"):
    """
    Save the specified image in the "fragments" folder.

    :param image: Image to save
    :param filename: A name for the image with the extension. If not specified the default is output_img.png
    :return:
    """
    folder_path = os.getcwd()
    temp_path = folder_path + "\images\\fragments" + filename
    try:
        cv2.imwrite(filename, image)
        print("Image saved successfully!")
    except:
        print("Error while saving image!")

def write_weights_on_file(image,sheet):

    width = image.get_image_width()
    height = image.get_image_height()

    for i in range(3, width - 1):  # bug
        for j in range(3, height - 1):
            pixel_color = image.get_pixel_color_BGR(Point(i, j))
            neighbors_black_color_percentage = image.get_percentage_of_black_neighbors(Point(i, j), 3)

            if (pixel_color.is_black()):
                # Pixel is black
                if (neighbors_black_color_percentage == 100):
                    # 1 Case: Background pixel
                    sheet.cell(row=i, column=j).value = MINIMUM_WEIGHT
                elif(neighbors_black_color_percentage >= 25 and neighbors_black_color_percentage <= 50):
                    # 2 Case: Edge pixel
                    sheet.cell(row=i, column=j).value = MEDIUM_WEIGHT
                else:
                    # 3 case: a pixel inside the image or "far" from the center of the matrix.
                    sheet.cell(row=i, column=j).value = MEDIUM_WEIGHT
            else:
                # A colored pixel. This must not be overwritten.
                sheet.cell(row=i, column=j).value = MAXIMUM_WEIGHT

    workbook.save("Excel_" + IMG_NAME + ".xlsx")

def create_border_layer(image,sheet):
    width = image.get_image_width()
    height = image.get_image_height()

    for i in range(3, width - 1):
        for j in range(3, height - 1):
            pixel_weight = sheet.cell(i, j).value
            if(pixel_weight == MEDIUM_WEIGHT):
                maximum_weight_pixels = image.get_maximum_weight_pixels(sheet,MAXIMUM_WEIGHT, Point(i,j))
                maximum_colors = []
                for element in maximum_weight_pixels:
                    maximum_colors.append(image.get_pixel_color_BGR(Point(element.get_x(),element.get_y())))

                blue_temp = []
                green_temp = []
                red_temp = []
                for color_temp in maximum_colors:
                    blue_temp.append(color_temp.get_blue())
                    green_temp.append(color_temp.get_green())
                    red_temp.append(color_temp.get_red())
                #    print("Red = {} - Green = {} -- Blue = {}".format(color.get_blue(),color.get_green(),color.get_red()))
                medium_blue = calculate_int_average(blue_temp)
                medium_green = calculate_int_average(green_temp)
                medium_red = calculate_int_average(red_temp)

                image.change_pixel_color(Point(i,j),BGR(medium_blue,medium_green,medium_red))






if __name__ == "__main__":
    # Open the desired image
    fragment_image = cv2.imread(get_img_path(IMAGE_NAME), cv2.IMREAD_COLOR)
    image = Image(fragment_image)

    # Initialize excel file
    excel_file = createExcel("Excel_" + IMG_NAME + ".xlsx")
    workbook = load_workbook(excel_file)
    sheet = workbook.active


    # Apply the algoritm
    write_weights_on_file(image,sheet)
    create_border_layer(image,sheet)

    MEDIUM_WEIGHT = 4

    write_weights_on_file(image, sheet)
    create_border_layer(image, sheet)

    MEDIUM_WEIGHT = 3

    write_weights_on_file(image, sheet)
    create_border_layer(image, sheet)


    MEDIUM_WEIGHT = 2

    write_weights_on_file(image, sheet)
    create_border_layer(image, sheet)

    # Show and save the result
    fragment_image = image.get_opencv_image()
    cv2.imshow('image', fragment_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    save_image(fragment_image,IMG_NAME + "_OUTPUT" + IMG_EXTENSION)

