
# Sound Quality:
First concatenate all files in each dataset:

Do steps below for each dataset (comp-o/nl and comp-a/nl in our case), to
concatenate all .wav files into one big file:
- `sudo apt-get install sox` (on linux)
- Go to CGN dataset folder containing wav files
- `sox *.wav results_name_dataset.wav`

Do the following steps to analyze the data:
- Copy/move the concatenated .wav dataset files to dataAnalysis/soundQuality
- Edit the variables in SS_wrapperfft.m to match the filenames of your generated files
- Run SS_wrapperfft.m with Matlab

The results:
![alt text][datasets_spectogram]

[datasets_spectogram]: https://github.com/thaije/spontaneous-vs-read-phone-recognition/blob/master/dataAnalysis/soundQuality/soundnorm_spectogram.jpg "Spectogram of two datasets"

# Dataset generation

## Dataset length
We compare two datasets from CGN: spontaneous speech and read speech. The datasets
are folder comp-o/nl and comp-n/nl in the CNG dataset. We also use a dataset
which is the combination of the two which we will generate in the next part.

The results of the initial analysis (genDataset/datasetSize.py) on these datasets is:

```
Analyzing dataset, consisting of folders: ['comp-o/nl/']
Processed 1 folder(s) with a total of 561 files
Total number of frames: 3698852441
Total duration: 231178 seconds
Average number of frames: 6593319
Average framerate: 16000
Average duration: 412 seconds


Analyzing dataset, consisting of folders: ['comp-a/nl/']
Processed 1 folder(s) with a total of 925 files
Total number of frames: 8609626251
Total duration: 538101 seconds
Average number of frames: 9307704
Average framerate: 16000
Average duration: 581 seconds
```

## Balancing datasets
As seen in the results above the datasets are not equal. Furthermore, we want
to compare three datasets which are all, as far as possible, roughly equal in number of
frames / seconds / speaker characteristics.
The final three datasets we want are:
- Read speech (comp-o)
- spontaneous speech (comp-a)
- Read and spontaneous combined (comp-x)

How to run:
- Go to genDataset folder
- Set the correct paths at the top of `balanceDatasets.py`
- Run `python balanceDatasets.py`

This will compare the two datasets, and reduce the biggest dataset to the same
size as the smaller one. The .wav and .ort files of the reduced dataset are
copied to the new folder which you specified in `balanceDatasets.py`.

### Output of the balancing script
```
comp-a/nl/ has more frames, shrinking...
Found solution

Balanced datasets:

Analyzing comp-o/nl/
Processed 561 files
Total number of frames: 3698852441
Total duration: 231178 seconds
Average number of frames: 6593319
Average framerate: 16000
Average duration: 412 seconds


Analyzing comp-a/nl/
Processed 398 files
Total number of frames: 3707080842
Total duration: 231692 seconds
Average number of frames: 9314273
Average framerate: 16000
Average duration: 582 seconds


comp-a/nl/ has been reduced
```

## Other Preprocessing

Kaldi requires unzipped .ort files. To unzip all .ort.gz files:
- Go into the folder with the .ort.gz files
- `gunzip *.ort.gz`

The script works with mono .wav files, to make all .wav files in a folder mono
execute the code below.
- Create a folder "mono"
- `for file in *.wav;do sox "$file" "mono/$file" remix -;done`
- Delete the old files, and move the files in /mono to the correct folder

## Generating comp-x
The general approach to this is summarized in this figure:
![alt text][genCompX]

[genCompX]: https://github.com/thaije/spontaneous-vs-read-phone-recognition/blob/master/dataAnalysis/genDataset/comp-x-generation.png "Generation of comp-x"
