interval = 0:15;
alpha = 2;

signal1 = zeros(1, 16);
signal2 = zeros(1, 16);
convolved_signal = zeros(1, 16);

for i = 1:16
    if i >= 1 && i <= 5
        signal1(i) = 1;
    end
    if i >= 1 && i <= 7
        signal2(i) = alpha^(i-1);
    end
end

for i = 1:16
    for j = 1:i
        convolved_signal(i) = convolved_signal(i) + signal2(j) * signal1(i-j+1);
    end
end

figure;
subplot(2, 2, 1);
stem(interval, signal1);
title('Signal x[n]');

subplot(2, 2, 2);
stem(interval, signal2);
title('Signal h[n]');

subplot(2, 2, 3);
stem(interval, convolved_signal);
title('Convolved Signal');

sgtitle('Convolution of Signals');







