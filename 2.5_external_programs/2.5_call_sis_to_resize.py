import os
import shutil
import subprocess


def resize():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ensure_dir(current_dir)
    source_dir = os.path.join(current_dir, "source")
    result_dir = os.path.join(current_dir, "result")
    for picture in os.listdir(source_dir):
        if picture.endswith(".jpg"):
            shutil.copyfile(os.path.join(source_dir, picture), os.path.join(result_dir, picture))
        else:
            print("{} это не картинка".format(picture))
    for picture in os.listdir(result_dir):
        subprocess.call(["sips", "--resampleWidth", "200", os.path.join(result_dir, picture)])


def ensure_dir(file_path):
    directory = os.path.join(file_path, "Result")
    if not os.path.exists(directory):
        os.makedirs(directory)


resize()
