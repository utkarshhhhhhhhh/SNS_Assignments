pi_value = pi;
inputs = -12*pi_value:0.1:12*pi_value;
outputs = cos(inputs/6) + sin(2*pi_value*inputs/3);

plot(inputs, outputs, 'm')
title('Continuous time plot of cos(t/6) + sin(2*pi*t/3)')
xlabel('t')
ylabel('y(t)')
grid on