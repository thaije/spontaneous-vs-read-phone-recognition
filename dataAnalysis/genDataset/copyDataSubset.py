#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Mon Oct 30 2017

@author: Tjalling Haije

This file copies receives a filelist of .wav files, and copies them to a
goalFolder along with the corresponding .ort files.
The .wav and .ort files are put in a wav and ort subfolder in the goalfolder.

"""

import shutil
import os



# wavFilelist   :  A filelist with paths to the new subset of wav files
# ortPath       :  Path to the ort files
# goalFolder    :  Folder to which the files should be copied
def copyDataSubset(wavFilelist, ortPath, goalFolder):

    wavFolder = goalFolder + "wav/"
    ortFolder = goalFolder + "ort/"

    filelist = []

    # create subfolders
    createFolder(wavFolder)
    createFolder(ortFolder)

    for wavFilePath in wavFilelist:

        # get filename without extension, and gen file names
        filename = os.path.splitext(os.path.basename(wavFilePath))[0]
        filelist.append(filename)
        wavFile = filename + ".wav"
        ortFile = filename + ".ort"

        # copy the .wav and .ort file to the destination folders
        shutil.copy(wavFilePath, wavFolder + wavFile)
        shutil.copy(ortPath + ortFile, ortFolder + ortFile)


    print ("Copying done")

    # create two files with a list of the files, easy for later use
    print ("\nFilelist generated in %s" % goalFolder + "files.txt")
    createFilelist(goalFolder + "files.txt", filelist)


# create a folder
def createFolder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)


# write a list to a file
def createFilelist(path, filelist):
    with open(path, 'wb') as f:
        for item in filelist:
            f.write("%s\n" % item)
