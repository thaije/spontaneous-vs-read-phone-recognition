import sys
import numpy as np
from scipy.io.wavfile import read
from matplotlib import pyplot as plt


def do_fft(received_wave, Fs=44100):
    """
    :param received_wave: wave file data.
    :param Fs: Sampling Rate, default = 44100
    :return: [Frequency, Amplitude]
    """

    # Calculating the fft coeff and amp sqrt(x^2+y^2)
    fft_coeff   = np.fft.fft(received_wave)
    Amp         = np.sqrt(np.abs(fft_coeff))


    print "FFT_coeff: ",fft_coeff
    print "Amp: ",Amp 

    # calulating size of recieved wave data and creating a freq array based on sampling freq Fs and size
    size1=len(received_wave)
    freq=np.linspace(0,Fs,size1)

    print "Length of recieved wave: ",size1;

    # Taking only half sample based on Nyquist-Shannon sampling theorem for ampiltude and frequency
    # https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem
    Amplitude  = Amp[0:int(size1/2)]
    Frequency = freq[0:int(size1/2)]


    print "\nAmplitude : ", Amplitude
    print "\nFreq : ", Frequency
    # This shorts the  index of the array in acending order
    idx = np.argsort(Amplitude)
    # freq1 is the maximum freq freq2 second maximum and so on
    freq1 = ((idx[-1]) / float(size1)) * Fs  
    freq2 = ((idx[-2]) / float(size1)) * Fs
    freq3 = ((idx[-3]) / float(size1)) * Fs

    return Amplitude, Frequency, freq1, freq2, freq3


def read_from_file(file_location):
    """
    Read file ad return audio data
    :param file_location: location of file.
    :return: audio data
    """

    data = read(file_location)


    # as scipy read function return two array [sample_rate_of_file, [audio_chunks]]
    sample_rate, audio_data = data
    print "Data: " ,data
    for i in range(len(audio_data)):
     #   print audio_data[i]
         pass

    print i
    return sample_rate, audio_data

def plot_fft(audio_file):

    # read audio chunks from audio file
    sample_rate, audio_data = read_from_file(audio_file)

    # call do_fft() function to get fft ( frequency and amplitude)
    Amplitude, Frequency, freq1, freq2, freq3 = do_fft(received_wave=audio_data, Fs=sample_rate)

    # plot fft
    plt.title("FFT heigest : {}, second_heigest : {}".format(freq1, freq2))
    plt.plot(Frequency, Amplitude)
    plt.show()
    plt.close()

    return True


if __name__ == '__main__':
    file = "fn001001.wav"
    plot_fft(file)