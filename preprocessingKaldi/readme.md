
# Pre-processing of CNG dataset for Kaldi

## Dependencies
- Numpy


## how to use:
Execute in the order as listed below. Execute code using python 3.

### Pre-pre-processing to generate input files for kaldi
- First in Kaldi_data_train.py, change the values of the following 3 variables
to the current folder:
    - data_folder (End with slash)
    - main_folder_wav (End with slash)
    - main_folder_annot (End with slash)
- Put unzipped .ort and .wav testfiles in testData/annot/... and testData/wav/... folders,
or point to the real CNG dataset.
    - .ort files such as from CGN2/data/annot/text/ort/comp-a/nl but unzipped(?)
    - .wav files such as from CGN2/data/audio/wav/comp-a/nl
- run Kaldi_data_train.py
- output is saved in 4 files in /train/

### Create list of phones from dataset
- In kaldi-phones.py change the values of 2 variables to the correct path, i.e. the testdata or real the CNG dataset:
    - datapath (End without slash)
    - phones_loc (End with slash)
E.g. change phones_loc="/home/tjalling/Desktop/ru/arm/preprocessingKaldi/phones-list/" to
      "/your/path/to/this/folder/preprocessingKaldi/phones-list/".
- Put the (awd or wrd) annotation files into the testData/annot/text/awd/... folder.
    - awd files such as from CGN2/data/annot/text/awd/comp-a/nl, both compressed as uncompressed work
- run kaldi-phones.py
- output is saved in 3 files in /phones-list/

### Create lexicon from dataset
- In kaldi-lexicon.py set the correct path to the testdata or the CNG dataset:
    - datapath (End without slash)
    - lex_loc (End without slash)
    - new_lex_loc (End without slash)
    - phones_loc (End without slash)
- run kaldi-lexicon.py
- output is 1 file in /lexicon/


# Pre-processing with Kaldi
