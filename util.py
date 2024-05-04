# files in folder

import os
import configparser


# os files function
def files_in_folder(input_folder):
    files = []
    for filename in os.listdir(input_folder):
        abs_path = os.path.join(input_folder, filename)
        files.append(abs_path)
    return files


def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config
