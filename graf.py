import time

import matplotlib.pyplot as plt
import numpy as np


def user_input(T: float, L: float, C: float, I: float) -> tuple:
    '''
    ввод данных
    -> время, индуктивность, ёмкость и силу тока
    <- T, L, C, I
    '''
    T = T * 10**(-6)
    L = L * 10**(-9)
    C = C * 10**(-3)
    I = I
    return T, L, C, I


def init_coord(T, L, C, I):
    '''
    создание массивов с координатами
    -> амплитудные значения: T, L, C, I
    <- массивы: t, q, i, Wc, Wl
    '''
    t = np.arange(0, T, 0.00000001)

    v = 1/(L * C)**0.5

    q = (I/v) * np.cos(v*t)
    i = I * np.cos(v*t + np.pi/2)
    Wc = q**2 / (2*C)
    Wl = (L * i**2) / 2

    return t, q, i, Wc, Wl


def generate_picture(x_values, y_values, x_label, y_label, name_frame) -> str:
    figure = plt.figure()

    axes = figure.add_axes([0.15, 0.1, 0.8, 0.8])
    axes.plot(x_values, y_values)
    axes.grid()

    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)

    picture_name = (
            f"Fiz_Graph_"+
            hex(int(str(time.time()).replace(".", "01"))).upper()+
            f"_{name_frame}.png")

    plt.savefig(picture_name)
    return picture_name


t_label = "Время t"
i_label = "Сила тока i"
q_label = "Заряд q"
Wm_label = "Магнитная энергия Wм"
Wl_label = "Электрическая энергия Wэ"

