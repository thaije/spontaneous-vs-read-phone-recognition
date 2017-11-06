#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Oct 29 2017

@author: Tjalling Haije

This file balances two datasets, so that they are roughly equal with regard
to the number of frames.
Each dataset consisting of a number of folders with .wav files in the
CNG dataset.

The dataset which was larger and thus shrunk, is copied to the specified folder.
Both the new subset of .wav files and .ort files.

Run with python3: python3 datasetSize.py

"""
import glob, wave, contextlib, random
from copyDataSubset import copyDataSubset

# basepath to the CGN dataset and .wav folders.
# NOTE: End with backslash
wavBasePath = '/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/CGN2/data/audio/wav/';
ortBasePath = '/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/CGN2/data/annot/text/ort/';

# datasets which are compared, a dataset can consist of multiple folders.
# NOTE: End with backslash
dataset1 = 'comp-o/nl/'
dataset2 = 'comp-a/nl/'

# Only the largest dataset will be reduced and copied to this folder.
# NOTE: End with backslash. Folders should be pre-existing
goalFolderD1 = '/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/reducedData/comp-o-reduced/'
goalFolderD2 = '/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/reducedData/comp-a-reduced/'

# declare some global variables
shrinkedDataset = False

# Datasets are seen as equal when the number of frames differes less than this
# number.
# Average number of frames for the files in the datasets is between 10million
# and 7million, so this should equalize the datasets within 1 audio file difference.
frameGoalDifference = 10000000


def estimateFolderSize(filelist, printResults):

    averageFrames = averageFrameRate = averageDuration = 0
    totalFrames = totalFrameRate = totalDuration = totalFiles = 0

    totalFiles += len(filelist)

    # loop through the files in the folder
    for filepath in filelist:

        # open file and get frames, framerate and duration
        with contextlib.closing(wave.open(filepath,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            #print("         File: Frames: %d, Framerate: %d, Duration %d" % (frames, rate, duration))

            totalFrames += frames
            totalFrameRate += rate
            totalDuration += duration


    averageFrames = totalFrames / float(totalFiles)
    averageFrameRate = totalFrameRate / float(totalFiles)
    averageDuration = totalDuration / float(totalFiles)

    if printResults:
        print ("Processed %d files" % (totalFiles))
        print ("Total number of frames: %d" % (totalFrames))
        print ("Total duration: %d seconds" % (totalDuration))
        print ("Average number of frames: %d" % (averageFrames))
        print ("Average framerate: %d" % (averageFrameRate))
        print ("Average duration: %d seconds" % (averageDuration))
        print ("\n")

    return [totalFrames, totalDuration]


def getFilelist(folder):
    folderPath = wavBasePath + folder
    return glob.glob(folderPath+"*.wav")


def balanceDatasets(dataset1, dataset2):
    global datasetShrinked
    global compxGoalFrames

    # get results of dataset 1
    print ("Analyzing %s" % dataset1)
    filelist1 = getFilelist(dataset1)
    [totalFrames1, totalDuration1] = estimateFolderSize(filelist1, True)

    # Get results of dataset 2
    print ("Analyzing %s" % dataset2)
    filelist2 = getFilelist(dataset2)
    [totalFrames2, totalDuration2] = estimateFolderSize(filelist2, True)

    print("------------------------------------")
    print("| Balancing datasets...            |")
    print("------------------------------------\n")

    # shrink dataset 2 if it is bigger
    if totalFrames2 > totalFrames1:
        print ("%s has more frames, shrinking... " % dataset2)
        shrinkedDataset = dataset2
        filelist2 = shrinkDataset(dataset2, filelist2, totalFrames1)
        compxGoalFrames = totalFrames1

    # shrink dataset 1 if it is bigger
    else:
        print ("%s has more frames. shrinking..." % dataset1)
        shrinkedDataset = dataset1
        filelist1 = shrinkDataset(dataset1, filelist1, totalFrames2)
        compxGoalFrames = totalFrames2

    # print new balanced results

    print("Balanced datasets:\n")
    print ("Analyzing %s" % dataset1)
    estimateFolderSize(filelist1, True)

    print ("Analyzing %s" % dataset2)
    estimateFolderSize(filelist2, True)

    return [filelist1, filelist2]

def shrinkDataset(dataset, originalFilelist, framesGoal):

    filelist = originalFilelist
    folderPath = wavBasePath + dataset

    # get the initial amount of frames
    [totalFrames, totalDuration] = estimateFolderSize(originalFilelist, False)

    # Try to get the frame difference between the datasets below this number
    while True:
        if abs(totalFrames - framesGoal) < frameGoalDifference:
            print ("Found solution\n")
            return filelist

        # Continue shrinking if the amount of frames is still bigger
        if totalFrames > framesGoal:
            # print ("Dataset still larger (%d frames above goal), continue shrinking" % (abs(totalFrames - framesGoal) - frameGoalDifference))
            # Get a random file from the filelist and remove it
            randomIndex = random.randint(0, len(filelist)-1)
            randomFile = filelist[randomIndex]
            filelist.remove(randomFile)
        # if it now is smaller, reset the filelist to the original and start over
        else:
            print ("Dataset shrank to much, resetting\n")
            filelist = originalFilelist

        # Do analysis of new filelist
        [totalFrames, totalDuration] = estimateFolderSize(filelist, False)

    # If not returned than we found no solution, maybe try making
    # frameGoalDifference larger
    print("No solution could be found for equalizing datasets.")
    return False




def main():
    # balance the datasets and get the new filelist back
    [filelistD1, filelistD2] = balanceDatasets(dataset1, dataset2)

    if shrinkedDataset is dataset1:
        ortPath = ortBasePath + dataset1
        print ("%s has been reduced\n" % dataset1)
        print ("Copying subset of %s to new folder %s" % (dataset1, goalFolderD1))
        copyDataSubset(filelistD1, ortPath, goalFolderD1)
    else:
        ortPath = ortBasePath + dataset2
        print ("%s has been reduced\n" % dataset2)
        print ("Copying subset of %s to new folder %s" % (dataset2, goalFolderD2))
        copyDataSubset(filelistD2, ortPath, goalFolderD2)




if __name__ == "__main__":
    main()
