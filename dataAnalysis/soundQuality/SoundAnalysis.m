% read audio file
[sig1,Fs1] = audioread('fn001604.wav');
[sig2,Fs2] = audioread('fn001619.wav');


[P1,f1] = periodogram(sig1,[],[],Fs1,'power');
[P2,f2] = periodogram(sig2,[],[],Fs2,'power');

subplot(2,1,1)
plot(f1,P1,'k')
grid
ylabel('P_1')
title('Power Spectrum')

subplot(2,1,2)
plot(f2,P2,'r')
grid
ylabel('P_2')
xlabel('Frequency (Hz)')
