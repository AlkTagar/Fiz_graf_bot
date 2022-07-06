#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gris

def user_input():
    T = float(input("Время в секундах t = "))
    L = float(input("Индуктивность катушки L = "))
    C = float(input("Электроёмкость конденсатора C = "))
    I = float(input("Сила тока I = "))
    return T, L, C, I


def init_coord(T, L, C, I):
    t = np.arange(0, T, 0.0001)
    
    v = 1/(L * C)**0.5

    q = (I/v) * np.cos(v*t)
    i = I * np.cos(v*t + np.pi/2)
    Wc = q**2 / 2*C
    Wl = (L * i**2) / 2

    return t, q, i, Wc, Wl


def my_plot_show(t, q, i, Wc, Wl):
    fig = plt.figure()
    gs = gris.GridSpec(2, 2)

    ti = fig.add_subplot(gs[0, 0])
    ti.plot(t, i)
    ti.grid()
    ti.set_xlabel("Время t")
    ti.set_ylabel("Сила тока i")

    tq = fig.add_subplot(gs[1, 0])
    tq.plot(t, q)
    tq.grid()
    tq.set_xlabel("Время t")
    tq.set_ylabel("Заряд q")

    tWl = fig.add_subplot(gs[0, 1])
    tWl.plot(t, Wl)
    tWl.grid()
    tWl.set_xlabel("Время t")
    tWl.set_ylabel("Магнитная энергия Wм")

    tWc = fig.add_subplot(gs[1, 1])
    tWc.plot(t, Wc)
    tWc.grid()
    tWc.set_xlabel("Значение времени t")
    tWc.set_ylabel("Электрическая энергия Wэ")

    plt.show()


def main():
    T, L, C, I = user_input()

    t, q, i, Wc, Wl = init_coord(T, L, C, L)

    my_plot_show(t, q, i, Wc, Wl)


if __name__ == "__main__":
    main()
