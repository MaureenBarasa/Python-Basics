import os

#creating a file with the command function "x" (Create Command). this command will create a new file if and only if there is no file already in existence with that name or else it will return an error.

#f = open("datatypes.py", "x")


#creating a text file with the command function "w"
f = open("demofile.txt", "w")

#This "w" command can also be used create a new file but unlike the the "x" command the "w" command will overwrite any existing file found with the same file name.


#create a folder
y = os.mkdir("myfolder")

#function to remove/delete a file

def remove_file_if_it_exists ():
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("the file does not exist")

remove_file_if_it_exists()


#function to check if a folder exists and if empty delete the folder

def remove_folder_if_it_exists():
   isdir = os.path.isdir("myfolder")
   if isdir == True:
       if len(os.listdir("myfolder")) == 0:
           os.rmdir("myfolder")
       else:
           print("the folder is not empty")
   else:
       print("the folder does not exist")

remove_folder_if_it_exists()














