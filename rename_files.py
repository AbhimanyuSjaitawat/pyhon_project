import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"A:\udacity\introduction to python\prank\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("current working directory is "+saved_path)
    os.chdir(r"A:\udacity\introduction to python\prank\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        print("old name - "+file_name);
        print("new name - "+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))

rename_files()    
