
# Pre-processing of CNG dataset for Kaldi

## Dependencies
- Numpy


## how to use:
### Pre-pre-processing to generate input files for kaldi
- First in Kaldi_data_train.py, change the values of the following 3 variables to the current folder:
    - data_folder (End with slash)
    - main_folder_wav (End with slash)
    - main_folder_annot (End with slash)
- Put .ort and .wav input files in /comp-o/nl/.
    - .ort files such as from CGN2/data/annot/text/ort/comp-a/nl but unzipped(?)
    - .wav files such as from CGN2/data/audio/wav/comp-a/nl
- run Kaldi_data_train.py
- output is saved in 4 files in output/train/

### Create list of phones from dataset
- In kaldi-phones.py change the values of two 2 variables to the path
of this folder + the suffix in the datapath. Change these two variables:
    - datapath (End without slash)
    - phones_loc (End with slash)
E.g. change datapath="/home/tjalling/Desktop/ru/arm/kaldi-test/phones-list-input/" to
      /your/path/to/this/folder/kaldi-test/phones-list-input/.
- Put the (awd or wrd) annotation files into the phones-list-input folder.
    - awd files such as from CGN2/data/annot/text/awd/comp-a/nl, both compressed as uncompressed work
- run kaldi-phones.py
- output is saved in 3 files in output/phones-list/

### Create lexicon from dataset
- In kaldi-lexicon.py change path values up to this folder in:
    - datapath (End without slash)
    - lex_loc (End without slash)
    - new_lex_loc (End without slash)
    - phones_loc (End without slash)
- run kaldi-lexicon.py
- output is 1 file in output/lexicon/


# Pre-processing with Kaldi
