import os
import shutil

from_dir = "/Users/rsingh/downloads"
to_dir = "/Users/rsingh/Project 102"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.pdf','.doc','.txt','.csv']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Image_files"
        path3 = to_dir + '/' + "Image_files" + '/' + file_name

        if os.path.exists(path2):
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)
        else : 
            os.mkdir(path2)
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)
