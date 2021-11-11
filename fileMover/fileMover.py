#This is a simple script that will allow you to copy all files from folders and subfolders
#using an extension of your choice to a specified Destination folder.

import os
import random
import shutil
from pathlib import Path
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog

#initialize Tkinter for folder selection
ws = Tk()
ws.withdraw()

def main():

    askMsg("Select SOURCE folder")
    sourceFolder = filedialog.askdirectory()
    askMsg("Select DESTINATION folder")
    destinationFolder = filedialog.askdirectory()
    fileExtension = askString()
    

    print(sourceFolder)
    print(destinationFolder)
    print(fileExtension)

    srcPath = sourceFolder
    srcDest = destinationFolder
    # srcPath = r'D:\xG\Heroes of Might and Magic 3 Complete\Maps\maps6000\1 - The Restoration of Erathia\1 - Small'
    # srcDest = r'D:\xG\Heroes of Might and Magic 3 Complete\Maps\maps6000\1 - The Restoration of Erathia'

    for root, dirs, files in os.walk(srcPath):
        for name in files:
            if name.endswith(fileExtension):
                try:
                    filePath = root + os.sep + name
                    filePathDestination = srcDest + os.sep + name
                    #Path(filePath).rename(filePathDestination)
                    shutil.move(filePath, filePathDestination)
                    print("Successfully moved: ", name)
                    #Path(filePath).rename(filePathDestination)
                    #shutil.move(filePath,srcDest)
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






