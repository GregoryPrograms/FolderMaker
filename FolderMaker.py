import os
import tkinter
from tkinter import filedialog
from pathlib import Path,PurePath

def main():
    tkinter.Tk().withdraw() # Close the root window
    dirPath = Path(filedialog.askdirectory(title = 'Select directory to sort...'))
    #List all files that aren't folders
    for root,_,files in os.walk(dirPath):
        for fileName in files:
            folderName = os.path.splitext(fileName)[0]
            os.mkdir(PurePath(root) / folderName)
            os.rename((PurePath(root) / fileName), (PurePath(root) / folderName / fileName))
if(__name__ == "__main__"):
    main()