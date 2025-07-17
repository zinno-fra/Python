"""
The following code is a simple file scanner. It can only take one file extension at a time, and is set before the code is ran. The output is sent to the command prompt in this version.
"""

import os #imports the os module

folder = "C:\\Users\\ithin\\Downloads"#set the folder to be scanned

target_extension = ".ova"#set extension looking for

#list all files in the folder
for file_name in os.listdir(folder):#starts loop that goes through each file and folder name inside folder specified | os.listdir(folder) gives a list of names of everything in 
                                    #that folder, files and subfolders. for file_name in means take each name one at a time and call it file_name, to then do something with filename inside the loop
    if file_name.lower().endswith(target_extension):#file_name.lower makes the name lowercase, .endswith checks the name endswith desired extension
        print(file_name)#name to print if matches desired extension