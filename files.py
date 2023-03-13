import os

#function to create folders from names on a list (check if folders exists and creates them if they do not exist)

def make_folders ():
    folders = ["myfolder1", "myfolder2"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

make_folders()


#creating a file with the command function "x" (Create Command). this command will create a new file if and only if there is no file already in existence with that name or else it will return an error.

#f = open("datatypes.py", "x")

#function to create files

def create_files ():
    f = open ("demofile.txt", 'w') #create file on current directory
    with open ("./myfolder2/demofile2.txt", "w") as file: #create a file on a specific folder and add data to the file
        file.write ("I am learning Python!\n")
        file.write ("I am really enjoying it!\n")
        file.write ("And I want to add more lines to say how much I like it")

create_files()

#the "w" command can also be used create a new file but unlike the the "x" command the "w" command will overwrite any existing file found with the same file name.

#function to remove/delete a file

def remove_file_if_it_exists ():
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("the file does not exist")

remove_file_if_it_exists()


#function to check if a folder exists and if empty delete the folder

def remove_folder_if_it_exists():
   isdir = os.path.isdir("myfolder1")
   if isdir == True:
       if len(os.listdir("myfolder1")) == 0:
           os.rmdir("myfolder1")
       else:
           print("the folder is not empty")
   else:
       print("the folder does not exist")

remove_folder_if_it_exists()















