import os 

input_dir = r"D:\Document\Python_Files\test"
rename = "TS2"

file_list = os.listdir(input_dir)

for filename in file_list:
    portion = os.path.splitext(filename)
    new_name = rename + portion[1]
    os.replace(filename, new_name)
