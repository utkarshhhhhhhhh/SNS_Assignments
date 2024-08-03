inputs = -48:6:48;

outputs = cos(inputs/6);

stem(inputs, outputs, 'filled')

% Set plot title, labels, and grid
title('Discrete time plot of cos[n/6]')
xlabel('n')
ylabel('y[n]')
grid on
