#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Oct 29 2017

@author: Tjalling Haije

This file compares the number of frames, framerate and duration of two
datasets. Each dataset consisting of a number of folders with .wav files in the
CNG dataset.

Run with python3: python3 datasetSize.py

"""
import glob, wave, contextlib, random

# basepath to the CGN dataset and .wav folders
wavBasePath = '/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/CGN2/data/audio/wav/';

# datasets which are compared, a dataset can consist of multiple folders
wav_dataset1 = 'comp-o/nl/'
wav_dataset2 = 'comp-a/nl/'

# declare some global variables
shrinkedDataset = False
compxGoalFrames = False

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


def balanceDatasets(wav_dataset1, wav_dataset2):
    global datasetShrinked
    global compxGoalFrames

    # get results of dataset 1
    print ("Analyzing %s" % wav_dataset1)
    filelist1 = getFilelist(wav_dataset1)
    [totalFrames1, totalDuration1] = estimateFolderSize(filelist1, True)

    # Get results of dataset 2
    print ("Analyzing %s" % wav_dataset2)
    filelist2 = getFilelist(wav_dataset2)
    [totalFrames2, totalDuration2] = estimateFolderSize(filelist2, True)

    print("------------------------------------")
    print("| Balancing datasets...            |")
    print("------------------------------------\n")

    # shrink dataset 2 if it is bigger
    if totalFrames2 > totalFrames1:
        print ("%s has more frames, shrinking... " % wav_dataset2)
        shrinkedDataset = wav_dataset2
        filelist2 = shrinkDataset(wav_dataset2, filelist2, totalFrames1)
        compxGoalFrames = totalFrames1

    # shrink dataset 1 if it is bigger
    else:
        print ("%s has more frames. shrinking..." % wav_dataset1)
        shrinkedDataset = wav_dataset1
        filelist1 = shrinkDataset(wav_dataset1, filelist1, totalFrames2)
        compxGoalFrames = totalFrames2

    # print new balanced results

    print("Balanced datasets:\n")
    print ("Analyzing %s" % wav_dataset1)
    estimateFolderSize(filelist1, True)

    print ("Analyzing %s" % wav_dataset2)
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




def generateCompX(filelistD1, filelistD2):
    print("------------------------------------")
    print("| Generating comp-x...             |")
    print("------------------------------------\n")


    compxFrames = 0
    filelistCompX = []
    filelist1 = filelistD1
    filelist2 = filelistD2

    # continue adding a file from each dataset(comp-o and comp-x) each loop, and
    # check if we are within an acceptable range of frames from the other two datasets
    while True:
        # check the difference with the goal number of frames
        if abs(compxFrames - compxGoalFrames) < frameGoalDifference:
            print ("Found solution\n")
            return filelistCompX

        # Add a file from each dataset
        if compxFrames < compxGoalFrames:
            # print ("Comp-x still smaller (%d frames below goal), continue adding" % (abs(compxFrames - compxGoalFrames) - frameGoalDifference))
            # Get a random file from both filelist
            randomIndex1 = random.randint(0, len(filelistD1)-1)
            randomIndex2 = random.randint(0, len(filelistD2)-1)

            # get the file with the random indices from both dataset filelists
            randomFile1 = filelist1[randomIndex1]
            randomFile2 = filelist2[randomIndex2]

            # add the files to comp-x with the prefix of the dataset it came from
            filelistCompX.append(randomFile1)
            filelistCompX.append(randomFile2)

            # remove file from other dataset filelist so we don't add them again
            filelist1.remove(randomFile1)
            filelist2.remove(randomFile2)

        # If we added too much files and have too much frames, reset and start over
        else:
            print ("Too much frames in comp-x, resetting\n")
            filelist1 = filelistD1
            filelist2 = filelistD2

        [compxFrames, compxDuration] = estimateFolderSize(filelistCompX, False)

    print("Couldn't find a solution, something is wrong")


def main():

    [dataset1, dataset2] = balanceDatasets(wav_dataset1, wav_dataset2)

    filelistCompX = generateCompX(dataset1, dataset2);

    print ("Analyzing comp-x")
    estimateFolderSize(filelistCompX, True)


if __name__ == "__main__":
    main()
