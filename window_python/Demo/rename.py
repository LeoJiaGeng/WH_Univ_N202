import os 
from files import ReFilenames

def rename():
    # Read a temporary directory
    input_dir = r"C:\Users\DELL\Desktop\transfer"
    file_list = os.listdir(input_dir)

    # input the list of new filenames
    rename1 = "11py-pc"
    rename2 = "TS8-1-r"
    rename_list = [rename1] * 3 + [rename2] * 3

    for filename, rename in zip(file_list, rename_list):
        # get the file suffix
        portion = os.path.splitext(filename)
        # combine the old file suffix with the new name
        new_name = rename + portion[1]
        print("{} --> {}".format(filename,new_name))
        # print(os.path.join(input_dir,filename))
        # replace file name
        os.replace(os.path.join(input_dir,filename), os.path.join(input_dir,new_name))

    print("Success!")

def remove():
    # Read a temporary directory
    input_dir = r"C:\Users\DELL\Desktop\C4xianan1"
    input_suffix = "log"
    file_obj = ReFilenames(input_suffix)
    delete_list = file_obj.get_all_files(input_dir)
    for delete_file in delete_list:
        os.remove(delete_file)
        print("{} file was delete!".format(delete_file))

    print("total {} files, Success!".format(len(delete_list)))

if __name__ == "__main__":
    # rename()
    remove()