inputs = -50:50;
outputs = zeros(size(inputs));
pi_value = pi;

for i = 1:length(inputs)
    arg = 8 * pi_value * inputs(i) / 31;
    ans = cos(arg);
    outputs(i) = ans;
end

stem(inputs, outputs, 'filled')
title('Discrete time plot of cos[8*pi*n/31]')
xlabel('n')
ylabel('y[n]')
grid on
