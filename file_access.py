import cv2
from os import path
import os


def get_base_path():
    this_file_path = path.realpath(__file__)
    base_path = path.abspath(
        path.join(this_file_path, '..')
    )
    return base_path


class FileAccess:
    base_path = get_base_path()

    @staticmethod
    def get_file(file_name: str):
        pic = \
            FileAccess.get_genuine_file(file_name) if file_name[4:7] == file_name[-7: -4] \
            else FileAccess.get_forged_file(file_name)
        return pic

    @staticmethod
    def get_forged_file(file_name: str):
        path_of_forged_signatures = \
            os.path.join(FileAccess.base_path, "sample_Signature", "forged")
        file_path = os.path.join(path_of_forged_signatures, file_name)
        pic = cv2.imread(file_path)
        return pic

    @staticmethod
    def get_genuine_file(file_name: str):
        path_of_genuine_signatures = \
            os.path.join(FileAccess.base_path, "sample_Signature", "genuine")
        file_path = os.path.join(path_of_genuine_signatures, file_name)
        pic = cv2.imread(file_path)
        return pic

    @staticmethod
    def get_files_of_person(name: str):
        if len(name) != 3:
            raise Exception(f"`{str}` is not a valid person ID ")

        path_of_original_signatures = os.path.join(FileAccess.base_path, "sample_Signature", "genuine")
        os.chdir(path_of_original_signatures)
        pic_names = os.listdir()
        filtered_pics = [pic for pic in pic_names if pic[-7:-4] == name]
        return [cv2.imread(pic_path) for pic_path in filtered_pics]

    @staticmethod
    def get_forged_of_person(name: str):
        if len(name) != 3:
            raise Exception(f"`{str}` is not a valid person ID ")

        path_of_forged_signatures = os.path.join(FileAccess.base_path, "sample_Signature", "forged")
        os.chdir(path_of_forged_signatures)
        pic_names = os.listdir()
        filtered_pics = [pic for pic in pic_names if pic[-7:-4] == name]
        return [cv2.imread(pic_path) for pic_path in filtered_pics]
