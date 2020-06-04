from utils import *
from Image import *
from excelFile import *

IMAGE_NAME = "frag_30_2.png"

if __name__ == "__main__":
    fragment_image = cv2.imread(get_img_path(IMAGE_NAME), cv2.IMREAD_COLOR)
    image = Image(fragment_image)

    height, width, color_levels = fragment_image.shape

    excel_file = createExcel("Excel3.xlsx")
    workbook = load_workbook(excel_file)
    sheet = workbook.active

    for i in range(3, width-1):
        for j in range(3, height-1):
            pixel_color = image.get_pixel_color_BGR(Point(i,j))
            #print(i,j)

            if(pixel_color.is_black()):
                neighbors_colors_percentage = image.get_percentage_of_black_neighbors(Point(i,j),3)
                #print(neighbors_colors_percentage)
                if(neighbors_colors_percentage == 100):
                    # 1 Case: Background pixel
                    sheet.cell(row=i,column=j).value = 0
                elif(neighbors_colors_percentage >=25 and neighbors_colors_percentage <= 75):
                    # 2 case: Edge pixel
                    sheet.cell(row=i,column=j).value = 5
                else:
                    # 3 case: a pixel inside the image or "far" from the center of the matrix.
                    sheet.cell(row=i, column=j).value = 5
            else:
                # A colored pixel. This must not be overwritten.
                sheet.cell(row=i, column=j).value = 10

    workbook.save("Excel3.xlsx")

    workbook = load_workbook(excel_file)
    sheet = workbook.active

    number_of_iterations = 1
    for iteration in range(1, number_of_iterations+1):
        for i in range(3, width-1):
            for j in range(3, height-1):
                pixel_weight = sheet.cell(i,j).value
                if(pixel_weight == 5):
                    neighbors_weight_values = image.get_neighbors_pixel_weight(Point(i,j))
                    zero_weight_counter = 0
                    for weight in neighbors_weight_values:
                        if(weight ==0):
                            zero_weight_counter += 1
                    if(zero_weight_counter >=3):
                        sheet.cell(row=i,column=j).value = 4

    number_of_iterations = 1
    for iteration in range(1, number_of_iterations + 1):
        for i in range(3, width - 1):
            for j in range(3, height - 1):
                pixel_weight = sheet.cell(i, j).value
                if (pixel_weight == 4):
                    neighbors_weight_values = image.get_neighbors_pixel_weight(Point(i, j))
                    zero_weight_counter = 0
                    for weight in neighbors_weight_values:
                        if (weight == 0):
                            zero_weight_counter += 1
                    if (zero_weight_counter >= 3):
                        sheet.cell(row=i, column=j).value = 3

    for i in range(3, width-1):
        for j in range(3, height-1):
            pixel_weight = sheet.cell(i, j).value
            if(pixel_weight == 4):
                image.change_pixel_color(Point(i,j),BGR(0,0,255))
            elif(pixel_weight == 3):
                image.change_pixel_color(Point(i, j), BGR(255, 0, 0))



    workbook.save("Excel3.xlsx")


    fragment_image = image.get_opencv_image()

    cv2.imshow('image', fragment_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    save_image(image)




