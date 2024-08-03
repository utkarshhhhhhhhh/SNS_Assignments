inputs = -12*pi:0.1:12*pi;
outputs = cos(inputs/6);

plot(inputs, outputs, 'g')
title('Continuous time plot of cos(t/6)')
xlabel('t')
ylabel('y(t)')
grid on