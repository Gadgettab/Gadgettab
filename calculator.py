import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk, messagebox

#  bg_color = '#000000'
bg_color = '#151515'

window = Tk()
window.title("Физический калькулятор")
window.geometry('900x650')

global Q_e

window['background'] = bg_color

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                        settings={'TCombobox':
                                      {'configure':
                                           {'selectbackground': '#blue',
                                            'fieldbackground': bg_color,
                                            'background': '#454545',
                                            'foreground': 'white'
                                            }}}
                        )

combostyle.theme_use('combostyle')

text_1 = Label(window, text="Введите известные значения", font=("Arial Bold", 45), bg=bg_color, fg='white')
text_1.place(x=10, y=10)

text_2 = Label(window, text="Не все поля должны быть заполнены", font=("Arial Bold", 20), bg=bg_color, fg='white')
text_2.place(x=170, y=70)

text_3 = Label(window, text="* - поля, обязательные для заполнения!", font=("Arial Bold", 15), bg=bg_color, fg='white')
text_3.place(x=225, y=103)

Q_temp = Label(window, text="Кол-во теплоты/Q:", font=("Arial Bold", 25), bg=bg_color, fg='white')
Q_temp.place(x=30, y=150)
Q_e = Entry(window, width=10, bg=bg_color, fg='white', font=("Arial Bold", 20))
Q_e.place(x=500, y=153, height=33)

q_mesure = Combobox(window, font=("Arial Bold", 20))
q_mesure['values'] = ('мДж', 'Дж', 'кДж', 'МДж')
q_mesure.current(1)
q_mesure.place(x=700, y=153, height=33, width=150)
q_mesure['state'] = 'readonly'

C_temp = Label(window, text="Удельная теплоёмкость/c:", font=("Arial Bold", 25), bg=bg_color, fg='white')
C_temp.place(x=30, y=200)
C_e = Entry(window, width=10, bg=bg_color, fg='white', font=("Arial Bold", 20))
C_e.place(x=500, y=203, height=33)

text_3 = Label(window, text="(Дж*кг)/°С", font=("Arial Bold", 20), bg=bg_color, fg='white')
text_3.place(x=700, y=203)

begin_temp = Label(window, text="Начальная температура/t  :", font=("Arial Bold", 25), bg=bg_color, fg='white')
begin_temp.place(x=30, y=250)
t_1_e = Entry(window, width=10, bg=bg_color, fg='white', font=("Arial Bold", 20))
t_1_e.place(x=500, y=253, height=33, )

ind_1 = Label(window, text="1", font=("Arial Bold", 13), bg=bg_color, fg='white')
ind_1.place(x=443, y=271)

text_4 = Label(window, text="°С", font=("Arial Bold", 20), bg=bg_color, fg='white')
text_4.place(x=700, y=253)

end_temp = Label(window, text="Конечная температура/t  :", font=("Arial Bold", 25), bg=bg_color, fg='white')
end_temp.place(x=30, y=300)
t_2_e = Entry(window, width=10, bg=bg_color, fg='white', font=("Arial Bold", 20))
t_2_e.place(x=500, y=303, height=33, )

ind_2 = Label(window, text="2", font=("Arial Bold", 13), bg=bg_color, fg='white')
ind_2.place(x=422, y=321)

text_5 = Label(window, text="°С", font=("Arial Bold", 20), bg=bg_color, fg='white')
text_5.place(x=700, y=303)

delta_temp = Label(window, text="Разница температур/Δt:", font=("Arial Bold", 25), bg=bg_color, fg='white')
delta_temp.place(x=30, y=350)
d_t_e = Entry(window, width=10, bg=bg_color, fg='white', font=("Arial Bold", 20))
d_t_e.place(x=500, y=353, height=33, )

text_5 = Label(window, text="°С", font=("Arial Bold", 20), bg=bg_color, fg='white')
text_5.place(x=700, y=353)

wheight = Label(window, text="Масса/m:", font=("Arial Bold", 25), bg=bg_color, fg='white')
wheight.place(x=30, y=400)
m_e = Entry(window, width=10, bg=bg_color, fg='white', font=("Arial Bold", 20))
m_e.place(x=500, y=403, height=33, )

m_mesure = Combobox(window, font=("Arial Bold", 20))
m_mesure['values'] = ('мг', 'г', 'кг', 'т')
m_mesure.current(2)
m_mesure.place(x=700, y=403, height=33, width=150)
m_mesure['state'] = 'readonly'

wheight = Label(window, text="* Тело нагревается или остывает?", font=("Arial Bold", 25), bg=bg_color, fg='white')
wheight.place(x=30, y=450)

t_dir = Combobox(window, font=("Arial Bold", 20))
t_dir['values'] = ('Нагревается', 'Остывает')
t_dir.current(0)
t_dir.place(x=600, y=458, height=33, width=250)
t_dir['state'] = 'readonly'


def _calculate():
    error = 0
    global Q
    global Q_m
    Q_m = q_mesure.get()
    if Q_e.get() != '':
        try:
            Q = int(Q_e.get())
        except:
            messagebox.showinfo('ERROR', 'Неправильно введено значение "Q"')
            error = 1
    else:
        Q = 'pass'

    global c
    if C_e.get() != '':
        try:
            c = int(C_e.get())
        except:
            messagebox.showinfo('ERROR', 'Неправильно введено значение "c"')
            error = 1
    else:
        c = 'pass'

    global t_1
    if t_1_e.get() != '':
        try:
            t_1 = int(t_1_e.get())
        except:
            messagebox.showinfo('ERROR', 'Неправильно введено значение "t₁"')
            error = 1
    else:
        t_1 = 'pass'

    global t_2
    if t_2_e.get() != '':
        try:
            t_2 = int(t_2_e.get())
        except:
            messagebox.showinfo('ERROR', 'Неправильно введено значение "t₂"')
            error = 1
    else:
        t_2 = 'pass'

    global d_t
    if d_t_e.get() != '':
        try:
            d_t = int(d_t_e.get())
        except:
            messagebox.showinfo('ERROR', 'Неправильно введено значение "Δt"')
            error = 1
    else:
        d_t = 'pass'

    global m
    global m_m
    m_m = m_mesure.get()
    if m_e.get() != '':
        try:
            m = int(m_e.get())
        except:
            messagebox.showinfo('ERROR', 'Неправильно введено значение "m"')
            error = 1
    else:
        m = 'pass'

    if error == 0:
        calculation(m, Q_m, Q, m_m)



def calculation(m, Q_m, Q, m_m):
    main_results = []
    if Q == 'pass':
        q_results = calculate_q(m, Q_m, c, t_1, t_2, d_t)
        main_results.append('Q|' + str(q_results))
        # print('Q: ' + str(q_results))

    if c == 'pass':
        c_results = calculate_c(Q, m, t_1, t_2, d_t)
        main_results.append('c|' + str(c_results))
        # print('c: ' + str(c_results))
    if t_1 == 'pass':
        t_1_results = calculate_t_1(Q, m, t_2, c)
        main_results.append('t_1|' + str(t_1_results))
        # print('t_1: ' + str(t_1_results))
    if t_2 == 'pass':
        t_2_results = calculate_t_2(Q, m, t_1, c)
        main_results.append('t_2|' + str(t_2_results))
        # print('t_2: ' + str(t_2_results))
    if d_t == 'pass':
        d_t_results = calculate_d_t(Q, m, t_1, t_2, c)
        main_results.append('d_t|' + str(d_t_results))
        # print('d_t: ' + str(d_t_results))
    if m == 'pass':
        m_results = calculate_m(Q, m_m, c, t_1, t_2, d_t)
        main_results.append('m|' + str(m_results))
        # print('m: ' + str(m_results))
    q_2 = Q
    c_2 = c
    t_1_2 = t_1
    t_2_2 = t_2
    d_t_2 = d_t
    m_2 = m
    for i in main_results:
        try:
            data = i.split('|')
            if data[0] == 'Q':
                q_2 = int(data[1])
            elif data[0] == 'c':
                c_2 = int(data[1])
            elif data[0] == 't_1':
                t_1_2 = int(data[1])
            elif data[0] == 't_2':
                t_2_2 = int(data[1])
            elif data[0] == 'd_t':
                d_t_2 = int(data[1])
            elif data[0] == 'm':
                m_2 = int(data[1])
        except:
            print('ERROR in lines 213-225')

    values = {'Q': q_2, 'c': c_2, 't_1': t_1_2, 't_2': t_2_2, 'd_t': d_t_2, 'm': m_2}

    if q_2 == 'pass':
        q_results = calculate_q(m, Q_m, c_2, t_1_2, t_2_2, d_t_2)
        values['Q'] = q_results
    if c_2 == 'pass':
        c_results = calculate_c(q_2, m_2, t_1_2, t_2_2, d_t_2)
        values['c'] = c_results
    if t_1 == 'pass':
        t_1_results = calculate_t_1(q_2, m_2, t_2_2, c_2)
        values['t_1'] = t_1_results
    if t_2 == 'pass':
        t_2_results = calculate_t_2(q_2, m_2, t_1_2, c_2)
        values['t_2'] = t_2_results
    if d_t == 'pass':
        d_t_results = calculate_d_t(q_2, m_2, t_1_2, t_2_2, c_2)
        values['d_t'] = d_t_results
    if m_2 == 'pass':
        m_results = calculate_m(q_2, m_m, c_2, t_1_2, t_2_2, d_t_2)
        values['m'] = m_results

    print(values)
    global reset
    global Q_dat
    global c_dat
    global t_1_dat
    global t_2_dat
    global d_t_dat
    global m_dat
    global q_m_dat
    global m_m_dat
    global t_dir_dat

    reset = Button(window, text="Сброс", command=dell, bg=bg_color, fg='white', font=("Arial Bold", 90))
    reset.place(x=30, y=505, height=125, width=840)

    Q_e.place(x=10000, y=10000, height=33)
    Q_dat = Label(window, text=str(values['Q']), font=("Arial Bold", 20), bg=bg_color, fg='white')
    Q_dat.place(x=500, y=153)

    C_e.place(x=10000, y=10000, height=33)
    c_dat = Label(window, text=str(values['c']), font=("Arial Bold", 20), bg=bg_color, fg='white')
    c_dat.place(x=500, y=203, height=33)

    t_1_e.place(x=10000, y=10000, height=33, )
    t_1_dat = Label(window, text=str(values['t_1']), font=("Arial Bold", 20), bg=bg_color, fg='white')
    t_1_dat.place(x=500, y=253, height=33)

    t_2_e.place(x=10000, y=10000, height=33, )
    t_2_dat = Label(window, text=str(values['t_2']), font=("Arial Bold", 20), bg=bg_color, fg='white')
    t_2_dat.place(x=500, y=303, height=33)

    d_t_e.place(x=10000, y=10000, height=33, )
    d_t_dat = Label(window, text=str(values['d_t']), font=("Arial Bold", 20), bg=bg_color, fg='white')
    d_t_dat.place(x=500, y=353, height=33, )

    m_e.place(x=10000, y=10000, height=33, )
    m_dat = Label(window, text=str(values['m']), font=("Arial Bold", 20), bg=bg_color, fg='white')
    m_dat.place(x=500, y=403, height=33, )

    q_mesure.place(x=10000, y=10000, height=33, width=150)
    q_m_dat = Label(window, text=str(q_mesure.get()), font=("Arial Bold", 20), bg=bg_color, fg='white')
    q_m_dat.place(x=700, y=153, height=33, width=150)

    m_mesure.place(x=10000, y=10000, height=33, width=150)
    m_m_dat = Label(window, text=str(m_mesure.get()), font=("Arial Bold", 20), bg=bg_color, fg='white')
    m_m_dat.place(x=700, y=403, height=33, width=150)

    t_dir.place(x=10000, y=10000, height=33, width=250)
    t_dir_dat = Label(window, text=str(t_dir.get()), font=("Arial Bold", 20), bg=bg_color, fg='white')
    t_dir_dat.place(x=600, y=458, height=33, width=250)



calculate = Button(window, text="Рассчитать", command=_calculate, bg=bg_color, fg='white', font=("Arial Bold", 90))
calculate.place(x=30, y=505, height=125, width=840)

def dell():
    reset.destroy()
    Q_dat.destroy()
    c_dat.destroy()
    t_1_dat.destroy()
    t_2_dat.destroy()
    d_t_dat.destroy()
    m_dat.destroy()
    q_m_dat.destroy()
    m_m_dat.destroy()
    t_dir_dat.destroy()

    Q_e.place(x=500, y=153, height=33)
    C_e.place(x=500, y=203, height=33)
    t_1_e.place(x=500, y=253, height=33)
    t_2_e.place(x=500, y=303, height=33, )
    d_t_e.place(x=500, y=353, height=33, )
    m_e.place(x=500, y=403, height=33, )
    q_mesure.place(x=700, y=153, height=33, width=150)
    m_mesure.place(x=700, y=403, height=33, width=150)
    t_dir.place(x=600, y=458, height=33, width=250)


def calculate_q(m, Q_m, c, t_1, t_2, d_t):
    Q_counter = 0
    if c != 'pass':
        Q_counter = Q_counter + 1
    if (t_2 != 'pass' and t_1 != 'pass') or d_t != 'pass':
        Q_counter = Q_counter + 1
    if m != 'pass':
        Q_counter = Q_counter + 1
        if m_m == 'мг':
            m = m / 1000000
        elif m_m == 'г':
            m = m / 1000
        elif m_m == 'т':
            m = m * 1000
    if Q_counter == 3:
        if t_1 != 'pass' and t_2 != 'pass':
            q_pre_result = c * m * (t_2 - t_1)
            q_result = q_pre_result
            if Q_m == 'мДж':
                q_result = q_pre_result * 1000
            elif Q_m == 'кДж':
                q_result = q_pre_result / 1000
            elif Q_m == 'МДж':
                q_result = q_pre_result / 1000000
            return q_result
        else:
            q_pre_result = c * m * d_t
            q_result = q_pre_result
            if Q_m == 'мДж':
                q_result = q_pre_result * 1000
            elif Q_m == 'кДж':
                q_result = q_pre_result / 1000
            elif Q_m == 'МДж':
                q_result = q_pre_result / 1000000
            return q_result
    else:
        return 'pass'


def calculate_c(Q, m, t_1, t_2, d_t):
    c_counter = 0
    if Q != 'pass':
        c_counter = c_counter + 1
        if Q_m == 'мДж':
            Q = Q / 1000
        elif Q_m == 'кДж':
            Q = Q * 1000
        elif Q_m == 'мДж':
            Q = Q * 1000000
    if (t_2 != 'pass' and t_1 != 'pass') or d_t != 'pass':
        c_counter = c_counter + 1
    if m != 'pass':
        c_counter = c_counter + 1
        if m_m == 'мг':
            m = m / 1000000
        elif m_m == 'г':
            m = m / 1000
        elif m_m == 'т':
            m = m * 1000
    if c_counter == 3:
        if t_1 != 'pass' and t_2 != 'pass':
            c_result = Q / (m * (t_2 - t_1))
            return c_result
        else:
            c_result = Q / (m * d_t)
            return c_result
    else:
        return 'pass'


def calculate_t_1(Q, m, t_2, c):
    t_1_counter = 0
    temp_dir = t_dir.get()
    if t_2 != 'pass' and d_t != 'pass':
        if temp_dir == 'Нагревается':
            return t_2 - d_t
        else:
            return t_2 + d_t

    else:
        if Q != 'pass':
            t_1_counter = t_1_counter + 1
            if Q_m == 'мДж':
                Q = Q / 1000
            elif Q_m == 'кДж':
                Q = Q * 1000
            elif Q_m == 'мДж':
                Q = Q * 1000000
        if c != 'pass':
            t_1_counter = t_1_counter + 1
        if t_2 != 'pass':
            t_1_counter = t_1_counter + 1
        if m != 'pass':
            t_1_counter = t_1_counter + 1
            if m_m == 'мг':
                m = m / 1000000
            elif m_m == 'г':
                m = m / 1000
            elif m_m == 'т':
                m = m * 1000
        if t_1_counter == 4:
            temp_dir = t_dir.get()
            if temp_dir == 'Нагревается':
                t_1_result = t_2 - Q / (m * c)
                return t_1_result
            else:
                t_1_result = t_2 + Q / (m * c)
                return t_1_result
        else:
            return 'pass'


def calculate_t_2(Q, m, t_1, c):
    t_2_counter = 0
    temp_dir = t_dir.get()
    if t_1 != 'pass' and d_t != 'pass':
        if temp_dir == 'Нагревается':
            return t_1 + d_t
        else:
            return t_1 - d_t
    if Q != 'pass':
        t_2_counter = t_2_counter + 1
        if Q_m == 'мДж':
            Q = Q / 1000
        elif Q_m == 'кДж':
            Q = Q * 1000
        elif Q_m == 'мДж':
            Q = Q * 1000000
    if c != 'pass':
        t_2_counter = t_2_counter + 1
    if t_1 != 'pass':
        t_2_counter = t_2_counter + 1
    if m != 'pass':
        t_2_counter = t_2_counter + 1
        if m_m == 'мг':
            m = m / 1000000
        elif m_m == 'г':
            m = m / 1000
        elif m_m == 'т':
            m = m * 1000
    if t_2_counter == 4:
        temp_dir = t_dir.get()
        if temp_dir == 'Нагревается':
            t_2_result = t_1 + Q / (m * c)
            return t_2_result
        else:
            t_2_result = t_1 - Q / (m * c)
            return t_2_result
    else:
        return 'pass'


def calculate_d_t(Q, m, t_1, t_2, c):
    d_t_counter = 0
    if t_1 != 'pass' and t_2 != 'pass':
        temp_dir = t_dir.get()
        if temp_dir == 'Нагревается':
            d_t_result = t_2 - t_1
            return d_t_result
        else:
            d_t_result = t_1 - t_2
            return d_t_result
    else:
        if Q != 'pass':
            d_t_counter = d_t_counter + 1
            if Q_m == 'мДж':
                Q = Q / 1000
            elif Q_m == 'кДж':
                Q = Q * 1000
            elif Q_m == 'мДж':
                Q = Q * 1000000
        if c != 'pass':
            d_t_counter = d_t_counter + 1
        if m != 'pass':
            d_t_counter = d_t_counter + 1
            if m_m == 'мг':
                m = m / 1000000
            elif m_m == 'г':
                m = m / 1000
            elif m_m == 'т':
                m = m * 1000
        if d_t_counter == 3:

            d_t_result = Q / (m * c)
            return d_t_result

        else:
            return 'pass'


def calculate_m(Q, m_m, c, t_1, t_2, d_t):
    m_counter = 0
    if Q != 'pass':
        m_counter = m_counter + 1
        if Q_m == 'мДж':
            Q = Q / 1000
        elif Q_m == 'кДж':
            Q = Q * 1000
        elif Q_m == 'мДж':
            Q = Q * 1000000
    if c != 'pass':
        m_counter = m_counter + 1
    if (t_2 != 'pass' and t_1 != 'pass') or d_t != 'pass':
        m_counter = m_counter + 1
    if m_counter == 3:
        if t_1 != 'pass' and t_2 != 'pass':
            temp_dir = t_dir.get()
            if temp_dir == 'Нагревается':
                m_pre_result = Q / (c * (t_2 - t_1))
                m_results = m_pre_result
                if m_m == 'мг':
                    m_results = m_pre_result / 1000000
                elif m_m == 'г':
                    m_results = m_pre_result / 1000
                elif m_m == 'т':
                    m_results = m_pre_result * 1000
                return m_results
            else:
                m_pre_result = Q / (c * (t_1 - t_2))
                m_results = m_pre_result
                if m_m == 'мг':
                    m_results = m_pre_result / 1000000
                elif m_m == 'г':
                    m_results = m_pre_result / 1000
                elif m_m == 'т':
                    m_results = m_pre_result * 1000
                return m_results
        else:
            m_pre_result = Q / (c * d_t)
            m_results = m_pre_result
            if m_m == 'мг':
                m_results = m_pre_result / 1000000
            elif m_m == 'г':
                m_results = m_pre_result / 1000
            elif m_m == 'т':
                m_results = m_pre_result * 1000
            return m_results
    else:
        return 'pass'


window.mainloop()
