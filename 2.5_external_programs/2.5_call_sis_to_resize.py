import os
import subprocess


def resize():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ensure_dir(current_dir)
    for picture in os.listdir(os.path.join(current_dir, "test")):
        if picture.endswith(".jpg"):
            print(picture)
            subprocess.call(["sips", "-z 200", "picture" "cp currentdir/result"])
        else:
            print("{} это не картинка".format(picture))


def ensure_dir(file_path):
    directory = os.path.join(file_path, "Result")
    if not os.path.exists(directory):
        os.makedirs(directory)


resize()
