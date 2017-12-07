# Influence of input type on phone recognition using a CNN
This is a repository containing our files for our research: "What is the influence of input type (read vs. spontaneous) on phone recognition in a deep convolutional neural network".
The research has been done for the masters course Advanced Research Methods from the Radboud University Nijmegen. The study was done by training a DNN model on either spontaneous speech,
read speech, or a combination of both, testing each model on the three types of speech. The dataset used in the Corpus Gesproken Nederlands (CGN) dataset. 


## Folders
- CGN: contains the Corpus Gesproken Nederlands dataset (not pushed due to size)
- Ponyland: general info on the ponyland servers from the RU university.
- dataAnalysis: Scripts to analyze, balance and generate used datasets


## Datasets
A comparison is made between Spontaneous and read speech. The dataset used
is the Corpus Gesproken Nederlands. To be specific folder comp-o/nl and comp-n/nl.
In addition a third balanced dataset comp-x is generated with half spontaneous
and half read speech.


### Data Analysis
[see findings of the dataset analysis here](dataAnalysis)


## Used model
The model which we used can be found [here](https://github.com/schemreier/DNNcm).
Aside from the data analysis and cleaning described in the dataAnalysis, is preprocessing
also done using Kaldi [in the script for the DNN training](https://github.com/schemreier/DNNcm).


## Usefull links:
- [The research proposal](https://docs.google.com/document/d/1pZWNGS6Ybt3M0pSRjHjkKqZ-X_zyD5Eld1MtMw-uO0Q/edit#heading=h.r7ohv33pr6lv)
- [The research proposal presentation](https://docs.google.com/presentation/d/1moxdcfoUTF0ivlOQkJ4nDlOWQRZFF_PeBAvEmR_P7yM/edit#slide=id.g279c6755aa_0_0)
- [Github repo with our used model](https://github.com/schemreier/DNNcm)
- [GitHub repo of Danny Merkx](https://github.com/DannyMerkx/CGN_speech_recognition)
- [Kaldi training acoustic model tutorial](https://www.eleanorchodroff.com/tutorial/kaldi/kaldi-training.html)
- [Kaldi force alignment tutorial](https://www.eleanorchodroff.com/tutorial/kaldi/kaldi-forcedalignment.html)


## Usefull papers:
- Siniscalchi, S. M., Yu, D., Deng, L., & Lee, H. (2012). Exploiting Deep Neural Networks for Detection-Based Speech Recognition, 106, 148–157.
- Scharenborg, O. (2010). Modeling the use of durational information in human spoken-word recognition. J Acoust Soc Am, 127(6), 3758–3770.
- Qian, Y. & Woodland, P. (2016). Very Deep Convolutional Neural Networks for Robust Speech Recognition.
- Abdel-Hamid, O., Mohamed, A., Jiang, H. \& Penn, G. (2012). Applying Convolutional Neural Networks concepts to hybrid NN-HMM model for speech recognition. Acoustics, Speech, and Signal Processing, 1988. ICASSP-88., 1988 International Conference on. 4277-4280. 10.1109/ICASSP.2012.6288864.
- Bengio, Y. \& Lecun, Y. (1997). Convolutional Networks for Images, Speech, and Time-Series.
