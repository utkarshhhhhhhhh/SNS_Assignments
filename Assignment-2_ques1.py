import matplotlib.pyplot as plt

def function_h(n):
    if n >= 2:
        return 0.8 ** n
    else:
        return 0

def function_x(n):
    if n >= 3:
        return 1
    else:
        return 0

interval = list(range(-10, 11))

Signal_1 = [function_h(i) for i in interval]
Signal_2 = [function_x(i) for i in interval]
Convolved_Signal = [0 for _ in interval]

for i in range(-10, 11):
    for j in range(-10, 11):
        if i-j >= -10 and i-j <= 10:
            Convolved_Signal[i + 10] += function_h(j) * function_x(i - j)

figure, axis = plt.subplots(2, 2)
axis[0, 0].stem(interval, Signal_1)
axis[0, 0].set_title("Function h[n] :")
axis[0, 1].stem(interval, Signal_2)
axis[0, 1].set_title("Function x[n] :")
axis[1, 0].stem(interval, Convolved_Signal)
axis[1, 0].set_title("Convolved Function :")
plt.show()

