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


int_folder = ("D:\maid movie\harry potter\www.TamilBlasters.ws - Harry Potter Octalogy (2001 to 2011)[720p - BDRip's - "
              "[Tamil + Telugu + Hindi + Eng] - x264 - 14GB]")

print(*files_in_folder(int_folder), sep='\n')


def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config
