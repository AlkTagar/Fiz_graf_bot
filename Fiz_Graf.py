import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gris


def user_input():
    '''
    ввод данных
    -> время, индуктивность, ёмкость и силу тока
    <- T, L, C, I
    '''
    T = float(input("Время в микросекундах t = "))
    L = float(input("Индуктивность в нанофарадах L = "))
    C = float(input("Электроёмкость в милигенри C = "))
    I = float(input("Сила тока в амперах I = "))
    return T * 10**(-6), L * 10**(-9), C * 10**(-3), I


def init_coord(T, L, C, I):
    '''
    создание массивов с координатами
    -> T, L, C, I
    <- t, q, i, Wc, Wl
    '''
    t = np.arange(0, T, 0.00000001)
    
    v = 1/(L * C)**0.5

    q = (I/v) * np.cos(v*t)
    i = I * np.cos(v*t + np.pi/2)
    Wc = q**2 / (2*C)
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
    t, q, i, Wc, Wl = init_coord(T, L, C, I)
    my_plot_show(t, q, i, Wc, Wl)


if __name__ == "__main__":
    main()
