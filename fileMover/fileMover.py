#This is a simple script that will allow you to copy all files from folders and subfolders
#using an extension of your choice to a specified Destination folder.

import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

#initialize Tkinter for folder selection and extension input
ws = Tk()
ws.withdraw()

def main():

    #asking for input folder and extension
    askMsg("Select SOURCE folder")
    sourceFolder = filedialog.askdirectory()
    askMsg("Select DESTINATION folder")
    destinationFolder = filedialog.askdirectory()
    
    fileExtension = askString()
    srcPath = sourceFolder
    srcDest = destinationFolder

    #for debug purposes
    print(sourceFolder)
    print(destinationFolder)
    print(fileExtension)

    #file mover algorithm
    for root, dirs, files in os.walk(srcPath):
        for name in files:
            if name.endswith(fileExtension):
                try:
                    filePath = root + os.sep + name
                    filePathDestination = srcDest + os.sep + name
                    shutil.move(filePath, filePathDestination)
                    print("Successfully moved: ", name)
                except UnicodeEncodeError:
                    print("-----------------Error")

def askMsg(message: str):
    response = messagebox.askokcancel('information', message)
    if (response == False):
        exit()

def askString():
    response = simpledialog.askstring("Extension Name", 'Enter extension name (including "."): ',parent = ws)
    return response


if __name__ == "__main__":
    main()






