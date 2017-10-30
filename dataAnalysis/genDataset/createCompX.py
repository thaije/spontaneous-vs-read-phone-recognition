
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Oct 30 2017

@author: Tjalling Haije

This file generates a new dataset comp-x from half comp-a and half comp-o.
The dataset is generated in two seperate parts: a train and test set.
The trianing set is generated from the train set of comp-a and comp-o.
The test set is generated from the test set of both.

The new generated filelists are then copied to specified folders

Run with python3: python3 createCompX.py

"""
import glob, wave, contextlib, random
from copyDataSubset import copyDataSubset


wavBasePath = '/home/tjalling/Desktop/ru/arm/data/';

trainD1 = wavBasePath + "trainset/wav/comp-o/"
trainD2 = wavBasePath + "trainset/wav/comp-a/"

testD1 = wavBasePath + "testset/wav/comp-o/"
testD2 = wavBasePath + "testset/wav/comp-a/"

goalFolderCompxTrain = "..."
goalFolderCompxTest = "..."

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



def generateCompX(filelistD1, filelistD2, compxGoalFrames):
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



def getFilelistFromFile(fname):

    with open(fname) as f:
        content = f.readlines()

    # We also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]


def main():

    ##############################################
    # Generate train set
    # get the filelist of both train sets
    filelistTrainD1 = getFilelistFromFile(trainD1)
    filelistTrainD2 = getFilelistFromFile(trainD2)

    # get filelist of the training set dataset 1 or 2
    [goalFramesTrainset, compxDuration] = estimateFolderSize(filelistTrainD1, False)

    # Generate the train set of comp-x
    filelistCompxTrain = generateCompX(filelistTrainD1, filelistTrainD2, goalFramesTrainset);

    copyDataSubset(dataset1, goalFolderCompxTrain)


    ##############################################
    # Generate test set
    # get the filelist of both train sets
    filelistTestD1 = getFilelistFromFile(testD1)
    filelistTestD2 = getFilelistFromFile(trainD2)

    # get filelist of the training set dataset 1 or 2
    [goalFramesTestset, compxDuration] = estimateFolderSize(filelistTestD1, False)

    # Generate the train set of comp-x
    filelistCompxTest = generateCompX(filelistTestD1, filelistTestD2, goalFramesTestset);

    copyDataSubset(dataset1, goalFolderCompxTest)


if __name__ == "__main__":
    main()
