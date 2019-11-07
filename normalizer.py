from numpy import ndarray
import cv2


class Normalizer:

    @classmethod
    def crop_make_binary_image(cls, image: ndarray):
        """
        crops the image so that the borders of the picture touch the signature. AND
        converts image to binary
        :type image: ndarray
        :return: numpy.ndarray
        """
        binary_image = cls.to_binary_image(image)

        original_width = binary_image.shape[1]
        original_height = binary_image.shape[0]

        min_width = original_width
        min_height = original_height
        max_height = 0
        max_width = 0

        for i in range(0, original_height):
            for j in range(0, original_width):
                if binary_image[i, j] == 0:
                    min_width = j if j < min_width else min_width
                    max_width = j if j > max_width else max_width
                    min_height = i if i < min_height else min_height
                    max_height = i if i > max_height else max_height
        return binary_image[min_height: max_height, min_width: max_width]

    @classmethod
    def to_binary_image(cls, image: ndarray):
        """
        converts image to B&W image
        :type image: numpy.ndarray
        :return: numpy.ndarray
        """
        gray_image = cls.to_gray(image)
        thresh, result = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
        return result
    
    @classmethod
    def to_gray(cls, image: ndarray):
        """
        receives a colored image and returns a gray scale image
        :type image: ndarray
        """
        if len(image.shape) < 3:
            return image
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @classmethod
    def resize(cls, width, height, image):
        return Normalizer.to_binary_image(  # seems resizing a binary image returns a gray scale image! why?? IDK
            cv2.resize(image, (width, height))
        )
