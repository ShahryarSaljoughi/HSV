import numpy

from normalizer import Normalizer
from signature_standards_specifier import SignatureStandardsSpecifier
from file_access import FileAccess


class Detector:

    @classmethod
    def is_signature_real(cls, signature_image_name: str) -> bool:
        person_id = signature_image_name[-7:-4]
        standards_specifier = SignatureStandardsSpecifier(person_id=person_id)
        standards = standards_specifier.get_standards()
        pic = Normalizer.resize(
            standards.width,
            standards.height,
            cls.__get_normalized_image(signature_image_name))
        number_of_pixels = Detector.__count_black_pixels(pic)
        return standards.pixel_low_bound < number_of_pixels < standards.pixel_high_bound

    @classmethod
    def __get_normalized_image(cls, signature_image_name: str) -> numpy.ndarray:
        raw_pic = FileAccess.get_file(signature_image_name)
        normalized = Normalizer.crop_make_binary_image(raw_pic)
        return normalized

    @classmethod
    def __count_black_pixels(cls, signature_image: numpy.ndarray) -> int:
        count = 0
        for i in range(signature_image.shape[0]):
            for j in range(signature_image.shape[1]):
                if signature_image[i, j] == 0:
                    count += 1
        return count

