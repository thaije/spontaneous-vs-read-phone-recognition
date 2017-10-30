#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Mon Oct 30 2017

@author: Tjalling Haije

This file copies all files in a filelist to a destination folder


"""

import shutil
import os


def copyDataSubset(filelist, goalFolder):

    for f in filelist:

        # get filename
        filename = os.path.basename(f)

        # copy to destination folder
        shutil.copy(f, goalFolder + filename)

    print ("Done")


# Example:
# filelist = ["/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/CGN2/data/audio/wav/comp-k/nl/fn001836.wav","/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/CGN2/data/audio/wav/comp-k/nl/fn001837.wav"]
# goalFolder = "/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/CGN2/data/audio/wav/comp-k/"
# copyDataSubset(filelist, goalFolder)
