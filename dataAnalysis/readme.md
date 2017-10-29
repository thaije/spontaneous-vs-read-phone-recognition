
# Sound Quality:
First concatenate all files in each dataset:

Do steps below for each dataset (nl of comp-o and comp-a in our case):
- `sudo apt-get install sox` (on linux)
- Go to CGN dataset folder containing wav files
- `sox *.wav results_name_dataset.wav`

Do the following steps to analyze the data:
- Copy/move the concatenated .wav dataset files to dataAnalysis/soundQuality
- Edit the variables in SoundAnalysis.m to match the filenames of your generated files
- Run SoundAnalysis.m with Matlab



# Dataset length
We compare two datasets from CGN: spontaneous speech and read speech. The datasets
are folder comp-o/nl and comp-n/nl in the CNG dataset. We also use a dataset
which is the combination of the two which we will generate in the next part.

The results of the analysis script (genDataset/datasetSize.py) on these datasets is:

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

# Creating equal datasets
As seen in the results above the datasets are not equal. Furthermore, we want
to compare three datasets which are all, as far as possible, roughly equal in number of
frames / seconds / speaker characteristics.
The final three datasets we want are:
- Read speech (comp-o)
- spontaneous speech (comp-a)
- Read and spontaneous combined (comp-x)

How to run:
- Go to genDataset folder
- Run `python3 CreateEqualDatasets.py`
