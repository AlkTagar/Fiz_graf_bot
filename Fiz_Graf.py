import time

import matplotlib.pyplot as plt
import numpy as np


def user_input(T, L, C, I):
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


def generate_picture(x_values, y_values, x_label, y_label, name_frame):
    figure = plt.figure()
    axes = figure.add_axes([0.15, 0.1, 0.8, 0.8])
    axes.plot(x_values, y_values)
    axes.grid()
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)
    picture_name = (
            f"Fiz_Graph_"+
            hex(int(str(time.time()).replace(".", "01"))).upper()+
            f"_{name_frame}.png"
            )
    plt.savefig(picture_name)


def my_plot_show(t, q, i, Wc, Wl):
    '''
    вывод графиков
    -> массивы t, q, i, Wc, Wl
    <- графики
    '''
    # график силы
    fig_I = plt.figure()
    ax_I = fig_I.add_axes([0.15, 0.1, 0.8, 0.8])
    ax_I.plot(t, i)
    ax_I.grid()
    ax_I.set_xlabel("Время t")
    ax_I.set_ylabel("Сила тока i")
    I_file_name = f"Fiz_I_graph_{int(time.time())}.png"
    plt.savefig(I_file_name)

    # график заряда
    fig_q = plt.figure()
    ax_q = fig_q.add_axes([0.15, 0.1, 0.8, 0.8])
    ax_q.plot(t, q)
    ax_q.grid()
    ax_q.set_xlabel("Время t")
    ax_q.set_ylabel("Заряд q")
    plt.savefig("Fiz_q_graph.png")

    # график маг энергии
    fig_Wl = plt.figure()
    ax_Wl = fig_Wl.add_axes([0.15, 0.1, 0.8, 0.8])
    ax_Wl.plot(t, Wl)
    ax_Wl.grid()
    ax_Wl.set_xlabel("Время t")
    ax_Wl.set_ylabel("Магнитная энергия Wм")
    plt.savefig("Fiz_Wl_graph.png")

    # график эл энергии
    fig_Wc = plt.figure()
    ax_Wc = fig_Wc.add_axes([0.15, 0.1, 0.8, 0.8])
    ax_Wc.plot(t, Wc)
    ax_Wc.grid()
    ax_Wc.set_xlabel("Значение времени t")
    ax_Wc.set_ylabel("Электрическая энергия Wэ")
    plt.savefig("Fiz_Wc_graph.png")


def graph(T, L, C, I):
    T, L, C, I = user_input(T, L, C, I)
    t, q, i, Wc, Wl = init_coord(T, L, C, I)
    my_plot_show(t, q, i, Wc, Wl)

