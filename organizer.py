import os
import shutil
#Taking an input for the path of the directory
path = input('Enter the name of the directory to be organized: ')

#To get the list of all the files is the mentioned directory
list_of_files = os.listdir(path)

#Going to each file & checking what kind of file it is
for i in list_of_files: 
    name, ext=os.path.splitext(i)

    #To store all the extension types - : - selects all
    ext=ext[1:]

    #If extension is empty - we have encountered another folder
    if ext=="": 
        continue

    #If folder already exists for this extension - move the file to the existing folder
    if os.path.exists(path+"/"+ext): 
        #shutil.move(source, destination)
        shutil.move(path+"/"+i, path+"/"+ext+"/"+i)

    #To create a new folder with the extension name - move the file to the new created folder
    else: 
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+i, path+"/"+ext+"/"+i)