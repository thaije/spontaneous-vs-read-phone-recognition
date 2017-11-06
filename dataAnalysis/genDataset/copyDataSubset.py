#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Mon Oct 30 2017

@author: Tjalling Haije

This file copies a filelist of files, and copies them to a goalFolder.

"""

import shutil
import os



# fielist   :   A filelist with paths to the new subset of files
# goalFolder:   Folder to which the files should be copied
def copyDataSubset(filelist, goalFolder):

    filenames = []

    # create subfolders
    createFolder(goalFolder)

    for filepath in filelist:

        # get filename without extension, and gen file names
        filename = os.path.basename(filepath)

        # save the filename for later
        filenames.append(filepath)

        # copy the file to the destination folder
        shutil.copy(filepath, goalFolder + filename)

    print ("Copying done")

    # create two files with a list of the files, easy for later use
    print ("Filelist generated in %s" % goalFolder + "files.txt")
    createFilelist(goalFolder + "files.txt", filenames)


# create a folder
def createFolder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)


# write a list with filenames to a file
def createFilelist(path, filelist):
    with open(path, 'w') as f:
        for item in filelist:
            f.write("%s\n" % item)
