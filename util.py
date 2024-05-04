# files in folder

import os
import configparser


# file functions
def files_in_folder(input_folder):
    files = []
    for filename in os.listdir(input_folder):
        files.append(filename)
    return files
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

# config functions
def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


# general util
def list_print(lis):
    print(*lis, sep='\n')

