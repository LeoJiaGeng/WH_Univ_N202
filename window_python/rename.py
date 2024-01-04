import os 

# Read a temporary directory
input_dir = r"C:\Users\DELL\Desktop\transfer"
file_list = os.listdir(input_dir)

# input the list of new filenames
rename1 = "TS3"
rename2 = "TS2"
rename_list = [rename1] * 3 + [rename2] * 3

for filename, rename in zip(file_list, rename_list):
    # get the file suffix
    portion = os.path.splitext(filename)
    # combine the old file suffix with the new name
    new_name = rename + portion[1]
    print(filename,new_name)
    # replace file name, 需要修改绝对路径
    os.replace(filename, new_name)

print("Success!")
