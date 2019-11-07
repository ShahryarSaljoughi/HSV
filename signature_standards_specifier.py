import cv2
from statistics import mean
from file_access import FileAccess
from normalizer import Normalizer


class SignatureStandard:
    def __init__(self, height, width, pixel_low_bound, pixel_high_bound):
        self.height = height
        self.width = width
        self.pixel_low_bound = pixel_low_bound
        self.pixel_high_bound = pixel_high_bound


class SignatureStandardsSpecifier:
    """
    this class specifies each person's signature how big is and specifies the average number of
    black pixels used in his signature
    """
    pass

    standards = {}

    def __init__(self, person_id: str) -> object:
        self.person = person_id
        if person_id not in self.__class__.standards:
            self.__class__.fill_person_info(person_id)

    def get_standards(self) -> SignatureStandard:
        return SignatureStandardsSpecifier.standards[self.person]

    @classmethod
    def fill_person_info(cls, person_id):
        if person_id in cls.standards:
            return

        signatures = FileAccess.get_files_of_person(person_id)
        normalized = [Normalizer.crop_make_binary_image(signature) for signature in signatures]
        average_height = round(mean([image.shape[0] for image in normalized]))
        average_width = round(mean([image.shape[1] for image in normalized]))
        scaled_to_standard_dimensions_signatures =\
            [Normalizer.resize(average_width, average_height, img) for img in normalized]

        def get_black_pixel_no(pic):
            count = 0
            for i in range(pic.shape[0]):
                for j in range(pic.shape[1]):
                    if pic[i, j] == 0:
                        count += 1
            return count

        number_of_black_pixels = \
            [get_black_pixel_no(pic) for pic in scaled_to_standard_dimensions_signatures]
        max_no_black_pixels = max(number_of_black_pixels)
        min_no_black_pixels = min(number_of_black_pixels)

        cls.standards[person_id] = \
            SignatureStandard(average_height, average_width, min_no_black_pixels, max_no_black_pixels)
