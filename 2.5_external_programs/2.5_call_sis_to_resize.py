import os
import subprocess


def resize():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ensure_dir(current_dir)
    for picture in os.listdir(os.path.join(current_dir, "source")):
        subprocess.call("cp {} {}".format(os.path.join(current_dir, picture), os.path.join(current_dir, "result",
                                                                                           picture)))
    for picture in os.listdir(os.path.join(current_dir, "result")):
        if picture.endswith(".jpg"):
            subprocess.call(["sips", "--resampleWidth", "200", os.path.join(current_dir, "result", picture)])
        else:
            print("{} это не картинка".format(picture))


def ensure_dir(file_path):
    directory = os.path.join(file_path, "Result")
    if not os.path.exists(directory):
        os.makedirs(directory)


resize()
