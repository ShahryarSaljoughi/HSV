import unittest
import cv2

from detector import Detector
from file_access import FileAccess
from normalizer import Normalizer
from signature_standards_specifier import SignatureStandard, SignatureStandardsSpecifier


class Tests(unittest.TestCase) :
    def test_file_access_get_base(self):
        path = FileAccess.get_base_path()
        self.assertEqual(path, "I:\\uni\\Machine Vision\\exercise2\\Signature")

    def test_get_files_of_person(self):
        pics = FileAccess.get_files_of_person("001")
        a = 3

    def test_normalizer_crop(self):
        pic = FileAccess.get_files_of_person("002")[0]
        cv2.imshow("pic", pic)
        cv2.waitKey(0)
        cropped = Normalizer.crop_make_binary_image(pic)

    def test_normalizer_gray_scale(self):
        pic = FileAccess.get_files_of_person("002")[0]
        Normalizer.to_gray(pic)

    def test_normalizer_to_black_and_white(self):
        pic = FileAccess.get_files_of_person("002")[0]
        pic = Normalizer.to_binary_image(pic)
        cv2.imshow("pic", pic)
        cv2.waitKey(0)

    def test_normalizer_crop(self):
        pic = FileAccess.get_files_of_person("002")[0]
        cropped = Normalizer.crop_make_binary_image(pic)
        cv2.imshow("original", pic)
        cv2.imshow("cropped", cropped)
        cv2.waitKey(0)

    def test_signature_standard_specifier(selft):
        standard = SignatureStandardsSpecifier("001").get_standards()

    def test_get_forged_file(self):
        pic = FileAccess.get_forged_file('NFI-00701023.png')
        cv2.imshow("pic", pic)
        cv2.waitKey(0)

    def test_detector_forged(self):
        file_name = 'NFI-00503015.png'
        result = Detector.is_signature_real(file_name)
        self.assertFalse(result)

    def test_detector_genuine(self):
        file_name = 'NFI-00302003.png'
        result = Detector.is_signature_real(file_name)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
