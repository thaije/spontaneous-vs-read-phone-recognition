#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Oct 22 2017

@author: Tjalling Haije

This file compares the number of frames, framerate and duration of two
datasets. Each dataset consisting of a number of folders with .wav files in the
CNG dataset.

Run with python3: python3 datasetSize.py

"""
import glob, wave, contextlib

# basepath to the CGN dataset and .wav folders
wavBasePath = '/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/CGN2/data/audio/wav/';

# datasets which are compared, a dataset can consist of multiple folders
wav_dataset1 = ['comp-o/nl/']
wav_dataset2 = ['comp-a/nl/']



def estimateFolderSize(folders):

    print ("Analyzing dataset, consisting of folders:", folders)

    averageFrames = averageFrameRate = averageDuration = 0
    totalFrames = totalFrameRate = totalDuration = totalFiles = 0

    # loop through the independent folders which make up the dataset
    for folder in folders:

        # get files in folder
        folderPath = wavBasePath + folder
        filelist=glob.glob(folderPath+"*.wav")

        totalFiles += len(filelist)
        #print("     Folder: %s contains %d files" % (folder, len(filelist)))


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

    print ("Processed %d folder(s) with a total of %d files" % (len(folders), totalFiles))
    print ("Total number of frames: %d" % (totalFrames))
    print ("Total duration: %d seconds" % (totalDuration))
    print ("Average number of frames: %d" % (averageFrames))
    print ("Average framerate: %d" % (averageFrameRate))
    print ("Average duration: %d seconds" % (averageDuration))
    print ("\n")


def main():
    estimateFolderSize(wav_dataset1)
    estimateFolderSize(wav_dataset2)


if __name__ == "__main__":
    main()
