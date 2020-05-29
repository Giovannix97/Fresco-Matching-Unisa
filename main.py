from utils import *
from Image import *


IMAGE_NAME = "black_white.png"

if __name__ == "__main__":
    fragment_image = cv2.imread(get_img_path(IMAGE_NAME), cv2.IMREAD_COLOR)

    cv2.imshow('image', fragment_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





