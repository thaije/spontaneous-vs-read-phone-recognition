
import glob, wave, contextlib, random, copy
from copyDataSubset import copyDataSubset

filelistBasePath = "/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/dataAnalysis/genDataset/filelists/comp-x-tjalling/"
trainFileOrt = filelistBasePath + "train/ort/files.txt"
trainFileWav = filelistBasePath + "train/wav/files.txt"

testFileOrt = filelistBasePath + "test/ort/files.txt"
testFileWav = filelistBasePath + "test/wav/files.txt"

goalFolder = "/home/tjalling/Desktop/ru/arm/spontaneous-vs-read-phone-recognition/CGN/generatedData/comp-x/"

# Read in the filepaths from the Kaldi generated file into a list
def getFilelistFromFile(fname):

    with open(fname) as f:
        content = f.readlines()

    # We also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content


def main():

    # read in filelists
    trainOrtFilelist = getFilelistFromFile(trainFileOrt)
    trainWavFilelist = getFilelistFromFile(trainFileWav)
    testOrtFilelist = getFilelistFromFile(testFileOrt)
    testWavFilelist = getFilelistFromFile(testFileWav)

    # check for duplicates
    from collections import Counter
    test = trainWavFilelist + testWavFilelist
    dupl = [k for k,v in Counter(test).items() if v>1]
    if len(dupl) != 0:
        print ("Found duplicates, fix your datasets")
    else
        print ("No duplicates found, good to go")

    # # make a folder with the data together
    # print ("Copying together 0%")
    # copyDataSubset(trainWavFilelist + testWavFilelist, goalFolder + "total/wav/comp-x/nl/")
    # print ("Copying together 50%")
    # copyDataSubset(trainOrtFilelist + testOrtFilelist, goalFolder + "total/ort/comp-x/nl/")
    # print ("Copying together 100%\n")
    #
    # # copy train
    # print ("Copying train 0%")
    # copyDataSubset(trainWavFilelist, goalFolder + "train/wav/comp-x/nl/")
    # print ("Copying train 50%")
    # copyDataSubset(trainOrtFilelist, goalFolder + "train/ort/comp-x/nl/")
    # print ("Copying train 100%\n")
    #
    # # copy test
    # print ("Copying test 0%")
    # copyDataSubset(testWavFilelist, goalFolder + "test/wav/comp-x/nl/")
    # print ("Copying test 50%")
    # copyDataSubset(testOrtFilelist, goalFolder + "test/ort/comp-x/nl/")
    # print ("Copying test 100%\n")



if __name__ == "__main__":
    main()
