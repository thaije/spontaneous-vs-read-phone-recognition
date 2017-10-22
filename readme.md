# Influence of input type on phone recognition using a CNN
This is a repository containing our files for our research: "What is the influence of input type (read vs. spontaneous) on phone recognition in a deep convolutional neural network".
The research has been done for the masters course Advanced Research Methods from the Radboud University Nijmegen.
It is based on research of Danny Merkx.


Preprocessing steps:
![alt text][preprocSteps]

[preprocSteps]: https://github.com/thaije/spontaneous-vs-read-phone-recognition/blob/master/Label%20preprocessing.jpg "Preprocessing steps"

## Folders
- CGN: contains the Corpus Gesproken Nederlands dataset (not pushed due to size)
- CGN_speech_recognition: The GitHub repository from our co-supervisor Danny Merkx, on which our research is based.
- preprocessingKaldi: The preprocessing to prepare the right files for Kaldi, based on code of Danny Merkx.
- Ponyland: general info on the ponyland servers from the RU university.
- dataAnalysis: Scripts to analyze and compare used datasets


## Datasets
A comparison is made between Spontaneous and read speech. The dataset used
is the Corpus Gesproken Nederlands. To be specific folder comp-o/nl and comp-n/nl.


### Data Analysis
[see the results here](dataAnalysis)


## Usefull links:
- [The research proposal](https://docs.google.com/document/d/1pZWNGS6Ybt3M0pSRjHjkKqZ-X_zyD5Eld1MtMw-uO0Q/edit#heading=h.r7ohv33pr6lv)
- [The research proposal presentation](https://docs.google.com/presentation/d/1moxdcfoUTF0ivlOQkJ4nDlOWQRZFF_PeBAvEmR_P7yM/edit#slide=id.g279c6755aa_0_0)
- [GitHub repo of Danny Merkx](https://github.com/DannyMerkx/CGN_speech_recognition)
- [Kaldi training acoustic model tutorial](https://www.eleanorchodroff.com/tutorial/kaldi/kaldi-training.html)
- [Kaldi force alignment tutorial](https://www.eleanorchodroff.com/tutorial/kaldi/kaldi-forcedalignment.html)

- [Diagram of the pipeline](https://www.draw.io/#G0B-IwinKF28akemphS3RaTGhsRjQ)

## Usefull papers:
- Siniscalchi, S. M., Yu, D., Deng, L., & Lee, H. (2012). Exploiting Deep Neural Networks for Detection-Based Speech Recognition, 106, 148–157.
- Scharenborg, O. (2010). Modeling the use of durational information in human spoken-word recognition. J Acoust Soc Am, 127(6), 3758–3770.
- Qian, Y. & Woodland, P. (2016). Very Deep Convolutional Neural Networks for Robust Speech Recognition.
- Abdel-Hamid, O., Mohamed, A., Jiang, H. \& Penn, G. (2012). Applying Convolutional Neural Networks concepts to hybrid NN-HMM model for speech recognition. Acoustics, Speech, and Signal Processing, 1988. ICASSP-88., 1988 International Conference on. 4277-4280. 10.1109/ICASSP.2012.6288864.
- Bengio, Y. \& Lecun, Y. (1997). Convolutional Networks for Images, Speech, and Time-Series.
