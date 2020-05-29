class Size:
    """
    A simple class to model two info of an image: height and width.
    """
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # Getters and setters
    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

