% Author: Steven Smits


function [periodogram, freqs] = SS_realtimefft(filename)
% Calculates power spectrum of audio input.
%periodogram output is the cumulative power over all timepoints, per frequency.
%freqs is frequency spectrum we actually measured.


%% Realtime audio analysis
frameLength = 16000; %16Khz Fs, so 1 sec per time
fileReader = dsp.AudioFileReader(...
    filename, ...
    'SamplesPerFrame', frameLength);

Fs = 16000;
Sr = Fs;
N = frameLength; %Number of samples per step
n = [1:N]'-1; %Samples N, 0 to N-1
nposfreqs = N/2+1; % number of positive frequencies
periodogram = zeros(nposfreqs,1); % Starting periodogram

fivemins = 5 * 60 * 16000; % So many frames for 5 mins processed.
countframes = 0; % Start with 0 frames
seconds = 0; % To normalize the periodogram later
tic
while ~isDone(fileReader)
    signal = step(fileReader); %Each step is a second; 16000 data points

    seconds = seconds +1;

    stereo = size(signal);
    stereo = stereo(2); % Check if stereo or mono
    if (stereo==2); signal = (signal(:,1)+signal(:,2))/2; end %Stereo to mono

     signal = (signal-mean(signal))/std(signal); % Normalize volume

    fftoutnorm=fft(signal)/N; % No normalized fourier
    fftoutnormposfreqs=fftoutnorm(1:nposfreqs); %Reducing the output size to only relevants.
    periodogram = periodogram + fftoutnormposfreqs.*conj(fftoutnormposfreqs); % Cumulative power over all time steps

    countframes = countframes + 16000; %Current amount of frames processed
    if rem(countframes, fivemins) == 0; % If five minutes has been processed
        minutes = countframes/16000/60; % Minutes analyzed
        text = strcat('Analyzed minutes:', {' '}, num2str(minutes));
        disp(text)
        text = strcat('In' ,{' '}, num2str(toc),{' '},'seconds');
        disp(text)
        fprintf('\n')


    end
end

% For plotting
Nyq=Sr/2; % Max frequency we can actually measure given our sample rate
duration=N/Sr; % Duration of every step (1 sec)
freqs=0:(1/duration):Nyq; %Frequencies we can measure given our sample rate and time window

periodogram = periodogram/seconds;
end
