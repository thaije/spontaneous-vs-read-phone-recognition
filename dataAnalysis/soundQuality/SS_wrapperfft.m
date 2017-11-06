% Author: Steven Smits
% File to create the periodograms of two large files, by reading them in
% in small chuncks. Normalized for volume, length etc.

[periodogram_o, freqs_o] = SS_realtimefft('results-o.wav');

[periodogram_a, freqs_a] = SS_realtimefft('results-a.wav');

figure()

% * volume normalized per second
% * ylims equal
% * Normalized per second power

% Plot power spectrum of results-o
subplot(2,2,1)
plot(freqs_o,periodogram_o, '-r','LineWidth', 2);
hold all
area(freqs_o,periodogram_o)
ylim([0, max([periodogram_a; periodogram_o]) + max([periodogram_a; periodogram_o])/4])

xlabel('Frequency (Hz)')
ylabel('Power')
title('Periodogram of results-o')

subplot(2,2,2)
plot(freqs_o,log(periodogram_o), '-r','LineWidth', 2);

maxy = max([log(periodogram_a); log(periodogram_o)]) - max([log(periodogram_a); log(periodogram_o)])/4;
miny = min([log(periodogram_a); log(periodogram_o)]) + min([log(periodogram_a); log(periodogram_o)])/4;
ylim([miny maxy])
xlabel('Frequency (Hz)')
ylabel('LOG(Power)')
title('LOG periodogram of results-o')

% Plot power spectrum of results-a
subplot(2,2,3)
plot(freqs_a,periodogram_a, '-r','LineWidth', 2);
hold all
area(freqs_a,periodogram_a)
ylim([0, max([periodogram_a; periodogram_o]) + max([periodogram_a; periodogram_o])/4])

xlabel('Frequency (Hz)')
ylabel('Power')
title('Periodogram of results-a')

subplot(2,2,4)
plot(freqs_a,log(periodogram_a), '-r','LineWidth', 2);
ylim([miny maxy])
xlabel('Frequency (Hz)')
ylabel('LOG(Power)')
title('LOG periodogram of results-a')
