
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


Paths Tjalling:

wavBasePath = '/vol/bigdata2/corpora2/CGN2/data/audio/wav/'
ortBasePath = '/vol/bigdata2/corpora2/CGN2/data/annot/text/ort/'

dataset1 = 'comp-o/nl/'
dataset2 = 'comp-a/nl/'

# set the path to the filelists of the other two datasets
filelistBasePath = '/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/dataAnalysis/genDataset/filelists/'

trainD1 = filelistBasePath + 'comp-o-train.txt'
trainD2 = filelistBasePath + 'comp-a-train.txt'

testD1 = filelistBasePath + 'comp-o-test.txt'
testD2 = filelistBasePath + 'comp-a-test.txt'

# folders which will contain the training and test set of comp-x
goalFolderCompxTrain = "/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/reducedData/comp-x/train/"
goalFolderCompxTest = "/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/reducedData/comp-x/test/"
"""
import glob, wave, contextlib, random, copy
from copyDataSubset import copyDataSubset

# paths for comp-o
wavBasePath = '/vol/bigdata2/corpora2/CGN2/data/audio/wav/';
ortBasePath = '/vol/tensusers/klux/text/ort/';

# paths for comp-a
wavBasePath2 = '/vol/tensusers/klux/reducedData/comp-a-reduced/mono_wav/';
ortBasePath2 = '/vol/tensusers/klux/reducedData/comp-a-reduced/ort/';

dataset1 = 'comp-o/nl/'
dataset2 = 'comp-a/nl/'

# set the path to the filelists of the other two datasets
filelistBasePath = '/vol/tensusers/klux/spontaneous-vs-read-phone-recognition/dataAnalysis/genDataset/filelists/'

trainD1 = filelistBasePath + 'comp-o-train.txt'
trainD2 = filelistBasePath + 'comp-a-train.txt'

testD1 = filelistBasePath + 'comp-o-test.txt'
testD2 = filelistBasePath + 'comp-a-test.txt'

# folders which will contain the training and test set of comp-x
goalFolderCompx = "/vol/tensusers/klux/comp-x/"


# Datasets are seen as equal when the number of frames differs less than this
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


# generate comp-x from half dataset 1 and half dataset 2
def generateCompX(filelistD1, filelistD2, compxGoalFrames):
    # print("------------------------------------")
    # print("| Generating comp-x...             |")
    # print("------------------------------------\n")


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


# Convert the list with paths to .wav files to the path to .ort files
def genOrtFilelist(filelist):

    for i in range(0,len(filelist)):
        filelist[i] = filelist[i].replace(wavBasePath, ortBasePath)
        filelist[i] = filelist[i].replace(wavBasePath2, ortBasePath2)

        # we already unzipped the files in the reducedData folder, take that in account
        if not "reducedData" in filelist[i]:
            filelist[i] = filelist[i].replace('.wav', '.ort.gz')
        else:
            filelist[i] = filelist[i].replace('.wav', '.ort')

    return filelist


# Read in the filepaths from the Kaldi generated file into a list
def getFilelistFromFile(fname):

    with open(fname) as f:
        content = f.readlines()

    # only keep the filepath
    for i in range(0, len(content)):
        content[i] = content[i].split()[-1]

    # We also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content



def main():

    print("------------------------------------")
    print("| Generating comp-x test set...    |")
    print("------------------------------------\n")

    # get the filelist of both train sets
    filelistTestD1 = getFilelistFromFile(testD1)
    filelistTestD2 = getFilelistFromFile(testD2)

    # get a goal number of frames for the comp-x test set from dataset 1 or 2
    [goalFramesTestset, compxDuration] = estimateFolderSize(filelistTestD1, False)

    # Generate the test set of comp-x
    filelistCompxTestWav = generateCompX(filelistTestD1, filelistTestD2, goalFramesTestset)
    filelistCompxTestOrt = genOrtFilelist(copy.copy(filelistCompxTestWav))

    # copy the files to the right folder
    print ("\nCopying .ort files of test set")
    copyDataSubset(filelistCompxTestOrt, goalFolderCompx + "test/ort/comp-x/nl/")
    print ("\nCopying .wav files of test set")
    copyDataSubset(filelistCompxTestWav, goalFolderCompx + "test/wav/comp-x/nl/")

    ##################################################
    print("\n------------------------------------")
    print("| Generating comp-x train set...   |")
    print("------------------------------------\n")

    # get the filelist of both train sets
    filelistTrainD1 = getFilelistFromFile(trainD1)
    filelistTrainD2 = getFilelistFromFile(trainD2)

    # get a goal number of frames for the comp-x training set from dataset 1 or 2
    [goalFramesTrainset, compxDuration] = estimateFolderSize(filelistTrainD1, False)

    # remove common files in both train and test sets
    filelistTrainD1 = list(set(filelistTrainD1).difference(filelistTestD1))
    filelistTrainD2 = list(set(filelistTrainD2).difference(filelistTestD2))

    # Generate the train set of comp-x
    filelistCompxTrainWav = generateCompX(filelistTrainD1, filelistTrainD2, goalFramesTrainset)
    filelistCompxTrainOrt = genOrtFilelist(copy.copy(filelistCompxTrainWav))

    # copy the files to the new training folder
    print ("\nCopying .ort files of train set")
    copyDataSubset(filelistCompxTrainOrt, goalFolderCompx + "train/ort/comp-x/nl/")
    print ("\nCopying .wav files of train set")
    copyDataSubset(filelistCompxTrainWav, goalFolderCompx + "train/wav/comp-x/nl/")


    ##################################################
    print("\n------------------------------------")
    print("| Generating comp-x total set...   |")
    print("------------------------------------\n")

    print ("\nCopying .ort files of total set")
    copyDataSubset(filelistCompxTrainOrt, goalFolderCompx + "total/ort/comp-x/nl/")
    print ("\nCopying .wav files of total set")
    copyDataSubset(filelistCompxTrainWav, goalFolderCompx + "total/wav/comp-x/nl/")


if __name__ == "__main__":
    main()
