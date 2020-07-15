from tkinter import *
from tkinter.colorchooser import askcolor  # Імпортуємо метод для вибору кольора

# Ініціюємо глобальні змінні
# Розмір шрифта
t_fontsize = r_fontsize = c_fontsize = 14

# Кольори фігур
triangle_color = 'green'  # Трикутник (зелений)
rectangle_color = 'blue'  # Прямокутник (блакитний)
circle_color = 'red'  # Коло (червоний)

# Колір опису зображень фігур
t_textcolor = 'green'  # Трикутник (зелений)
r_textcolor = 'blue'  # Прямокутник (блакитний)
c_textcolor = 'red'  # Коло (червоний)

# Блок координат для налаштувань
t_coords = [50, 200, 340, 200, 110, 60]  # Трикутник
r_coords = [80, 50, 320, 200]  # Прямокутник
c_coords = [100, 50, 300, 250]  # Коло


class ImageSettings(Frame):
    # Создає діалогове вікно налаштувань зображеннь
    def __init__(self, parent):
        Frame.__init__(self, parent)
        # Ініціалізація змінних
        self.t_color = 'yellow'
        self.r_color = 'blue'
        self.c_color = 'red'
        self.text_c4 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_c4 = Label(self, text="y2")
        self.text_c3 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_c3 = Label(self, text="x2")
        self.text_c2 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_c2 = Label(self, text="y1")
        self.text_c1 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_c1 = Label(self, text="x1")
        self.label_c = Label(self, text="Задати координати кола")
        self.frame_c = Frame(self, border=1, relief=SUNKEN, width=100, height=100)
        self.btn_c = Button(self, text="Оберить колір", command=lambda: self.onChoose_c())
        self.label_c_main = Label(self, text="Налаштування прямокутника")
        self.text_r4 = Entry(self, width=3, bg='#fff',  borderwidth=1)
        self.label_r4 = Label(self, text="y2")
        self.text_r3 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_r3 = Label(self, text="x2")
        self.text_r2 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_r2 = Label(self, text="y1")
        self.text_r1 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_r1 = Label(self, text="x1")
        self.label_r = Label(self, text="Задати координати прямокутника")
        self.frame_r = Frame(self, border=1, relief=SUNKEN, width=100, height=100)
        self.btn_r = Button(self, text="Оберить колір", command=lambda: self.onChoose_r())
        self.label_r_main = Label(self, text="Налаштування прямокутника")
        self.text_t6 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_t6 = Label(self, text="y3")
        self.text_t5 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_t5 = Label(self, text="x3")
        self.text_t4 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_t4 = Label(self, text="y2")
        self.text_t3 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_t3 = Label(self, text="x2")
        self.text_t2 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_t2 = Label(self, text="y1")
        self.text_t1 = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.label_t1 = Label(self, text="x1")
        self.label_t = Label(self, text="Задати координати трикутника")
        self.frame_t = Frame(self, border=1, relief=SUNKEN, width=100, height=100)
        self.btn_t = Button(self, text="Оберить колір", command=lambda: self.onChoose_t())
        self.btn_cancel = Button(self, text="Скасувати", command=lambda: self.cancel())
        self.btn_save = Button(self, text="Зберегти", command=lambda: self.save())
        self.label_t_main = Label(self, text="Налаштування трикутника")
        self.parent = parent
        self.initUI()

    def initUI(self):
        # Розташування елементів
        self.parent.title("Налаштування зображень")
        self.pack(fill=BOTH, expand=1)
        self.btn_cancel.place(x=400, y=400)
        self.btn_save.place(x=320, y=400)
        # Налаштування трикутника
        self.label_t_main.place(x=30, y=5)
        self.btn_t.place(x=30, y=30)
        self.frame_t.place(x=130, y=30)
        self.label_t.place(x=250, y=30)

        self.label_t1.place(x=250, y=50)
        self.text_t1.place(x=245, y=70)
        self.label_t2.place(x=290, y=50)
        self.text_t2.place(x=285, y=70)
        self.label_t3.place(x=330, y=50)
        self.text_t3.place(x=325, y=70)
        self.label_t4.place(x=370, y=50)
        self.text_t4.place(x=365, y=70)
        self.label_t5.place(x=410, y=50)
        self.text_t5.place(x=405, y=70)
        self.label_t6.place(x=450, y=50)
        self.text_t6.place(x=445, y=70)

        # Налаштування прямокутника
        self.label_r_main.place(x=30, y=135)
        self.btn_r.place(x=30, y=160)
        self.frame_r.place(x=130, y=160)
        self.label_r.place(x=250, y=160)

        self.label_r1.place(x=250, y=180)
        self.text_r1.place(x=245, y=200)
        self.label_r2.place(x=290, y=180)
        self.text_r2.place(x=285, y=200)
        self.label_r3.place(x=330, y=180)
        self.text_r3.place(x=325, y=200)
        self.label_r4.place(x=370, y=180)
        self.text_r4.place(x=365, y=200)

        # Налаштування кола
        self.label_c_main.place(x=30, y=265)
        self.btn_c.place(x=30, y=290)
        self.frame_c.place(x=130, y=290)
        self.label_c.place(x=250, y=290)

        self.label_c1.place(x=250, y=310)
        self.text_c1.place(x=245, y=330)
        self.label_c2.place(x=290, y=310)
        self.text_c2.place(x=285, y=330)
        self.label_c3.place(x=330, y=310)
        self.text_c3.place(x=325, y=330)
        self.label_c4.place(x=370, y=310)
        self.text_c4.place(x=365, y=330)

    def onChoose_t(self):
        """Обираємо колір для трикутника"""
        (rgb, hx) = askcolor()
        self.frame_t.config(bg=hx)
        self.t_color = hx

    def onChoose_r(self):
        """Обираємо колір для прямокутника"""
        (rgb, hx) = askcolor()
        self.frame_r.config(bg=hx)
        self.r_color = hx

    def onChoose_c(self):
        """Обираємо колір для кола"""
        (rgb, hx) = askcolor()
        self.c_color = hx
        self.frame_c.config(bg=hx)

    def cancel(self):
        """Зачиняємо вікно"""
        self.parent.destroy()

    def save(self):
        """ Функція зберігає налаштування обрані коритсувачем """
        # Зберігаємо координати трикутника
        global t_coords, r_coords, c_coords, triangle_color, rectangle_color, circle_color
        t_coords[0] = self.text_t1.get()
        t_coords[1] = self.text_t2.get()
        t_coords[2] = self.text_t3.get()
        t_coords[3] = self.text_t4.get()
        t_coords[4] = self.text_t5.get()
        t_coords[5] = self.text_t6.get()
        triangle_color = self.t_color
        # Зберігаємо координати прямокутника
        r_coords[0] = self.text_r1.get()
        r_coords[1] = self.text_r2.get()
        r_coords[2] = self.text_r3.get()
        r_coords[3] = self.text_r4.get()
        rectangle_color = self.r_color
        # Зберігаємо координати кола
        t_coords[0] = self.text_c1.get()
        t_coords[1] = self.text_c2.get()
        t_coords[2] = self.text_c3.get()
        t_coords[3] = self.text_c4.get()
        circle_color = self.c_color
        # Зачиняемо вікно
        self.parent.destroy()


class TextSettings(Frame):
    """ Создає діалогове вікно налаштувань тексту"""
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.t_fsize = 14
        self.t_tcolor = 'green'
        self.r_fsize = 14
        self.r_tcolor = 'blue'
        self.c_fsize = 14
        self.c_tcolor = 'red'
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Налаштування тексту")
        self.pack(fill=BOTH, expand=1)
        self.btn_cancel = Button(self, text="Скасувати", command=lambda: self.cancel())
        self.btn_cancel.place(x=160, y=215)
        self.btn_save = Button(self, text="Зберегти", command=lambda: self.save())
        self.btn_save.place(x=60, y=215)
        # Налаштування трикутника
        self.label_tc = Label(self, text="Налаштування трикутника")
        self.label_tc.place(x=5, y=5)
        self.frame_tc = Frame(self, border=1, relief=SUNKEN, width=25, height=25)
        self.frame_tc.place(x=100, y=35)
        self.btn_tc = Button(self, text="Оберить колір", command=lambda: self.onChoose_t())
        self.btn_tc.place(x=5, y=35)
        self.label_tf = Label(self, text="Оберить розмір тесту")
        self.label_tf.place(x=130, y=35)
        self.text_tf = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.text_tf.place(x=260, y=35)

        # Налаштування прямокутника
        self.label_rc = Label(self, text="Налаштування прямокутника")
        self.label_rc.place(x=5, y=75)
        self.frame_rc = Frame(self, border=1, relief=SUNKEN, width=25, height=25)
        self.frame_rc.place(x=100, y=105)
        self.btn_rc = Button(self, text="Оберить колір", command=lambda: self.onChoose_r())
        self.btn_rc.place(x=5, y=105)
        self.label_rf = Label(self, text="Оберить розмір тесту")
        self.label_rf.place(x=130, y=105)
        self.text_rf = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.text_rf.place(x=260, y=105)

        # Налаштування кола
        self.label_cc = Label(self, text="Налаштування кола")
        self.label_cc.place(x=5, y=145)
        self.frame_cc = Frame(self, border=1, relief=SUNKEN, width=25, height=25)
        self.frame_cc.place(x=100, y=175)
        self.btn_cc = Button(self, text="Оберить колір", command=lambda: self.onChoose_c())
        self.btn_cc.place(x=5, y=175)
        self.label_cf = Label(self, text="Оберить розмір тесту")
        self.label_cf.place(x=130, y=175)
        self.text_cf = Entry(self, width=3, bg='#fff', borderwidth=1)
        self.text_cf.place(x=260, y=175)

    def onChoose_t(self):
        """Обираємо колір для тексту трикутника"""
        (rgb, hx) = askcolor()
        self.frame_tc.config(bg=hx)
        self.t_tcolor = hx

    def onChoose_r(self):
        """Обираємо колір для тексту прямокутника"""
        (rgb, hx) = askcolor()
        self.frame_rc.config(bg=hx)
        self.r_tcolor = hx

    def onChoose_c(self):
        """Обираємо колір для тексту кола"""
        (rgb, hx) = askcolor()
        self.frame_cc.config(bg=hx)
        self.c_tcolor = hx

    def cancel(self):
        """Зачиняємо вікно"""
        self.parent.destroy()

    def save(self):
        """ Функція зберігає налаштування обрані коритсувачем """
        global t_textcolor, t_fontsize, r_textcolor, r_fontsize, c_textcolor, c_fontsize
        # Зберігаємо дані трикутника
        t_textcolor = self.t_tcolor
        t_fontsize = self.text_tf.get()
        # Зберігаємо дані прямокутника
        r_textcolor = self.r_tcolor
        r_fontsize = self.text_rf.get()
        # Зберігаємо дані кола
        c_textcolor = self.c_tcolor
        c_fontsize = self.text_cf.get()
        # Зачиняємо вікно
        self.parent.destroy()



def triangle():
    """Функція відображення трикутника"""
    # Прибираємо коло
    canvas.coords(c, (0, 0, 0, 0))
    canvas.coords(r, (0, 0, 0, 0))
    canvas.itemconfig(t, fill=triangle_color, outline='white')
    canvas.coords(t, (t_coords[0], t_coords[1], t_coords[2],
                      t_coords[3], t_coords[4], t_coords[5]))
    text.delete(1.0, END)
    text.insert(1.0, 'Зображення трикутника')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', t_fontsize), foreground=t_textcolor)


def rectangle():
    """Функція відображення прямокутника"""
    # Прибираємо коло
    canvas.coords(c, (0, 0, 0, 0))
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.itemconfig(r, fill=rectangle_color, outline='white')
    canvas.coords(r, (r_coords[0], r_coords[1], r_coords[2], r_coords[3]))
    text.delete(1.0, END)
    text.insert(1.0, 'Зображення прямокутника')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', r_fontsize), foreground=r_textcolor)


def circle():
    """Функція відображення кола"""
    # Скриваємо трикутник
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    # Скриваємо прямокутник
    canvas.coords(r, (0, 0, 0, 0))
    # Задаємо червоний колір колу и білий фону
    canvas.itemconfig(c, fill=circle_color, outline='white')
    # Задаємо координати для відображення кола
    canvas.coords(c, (c_coords[0], c_coords[1], c_coords[2], c_coords[3]))
    # Очищуємо поле з описанням
    text.delete(1.0, END)
    # Вставляємо опис зображення кола
    text.insert(1.0, 'Зображення кола')
    # Конфігуруємо позицію, шрифт(Times, розмір 14 за умовчанням) та колір (чорний за умовчанням)
    # для опису зображення кола
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', c_fontsize), foreground=c_textcolor)


def clear():
    """Функція очищення канви"""
    # Прибираємо трикутник
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    # Прибираємо прямокутник
    canvas.coords(r, (0, 0, 0, 0))
    # Прибираємо коло
    canvas.coords(c, (0, 0, 0, 0))
    # Очищуємо поле з описом
    text.delete(1.0, END)


def image_settings():
    """Функція відображає вікно налаштувань зображеннь"""
    settings = Toplevel()        # Нове вікно
    s = ImageSettings(settings)  # Відібраження налаштувань
    settings.geometry("500x450+200+200")   # Встановлюємо розміри вікна

    settings.grab_set()      ##################
    settings.focus_set()     # Контроль фокуса вікна
    settings.wait_window()   ##################

    settings.mainloop()


def text_settings():
    """Функція відображає вікно налаштувань тексту"""
    settings = Toplevel()  # Нове вікно
    s = TextSettings(settings)  # Відібраження налаштувань
    settings.geometry("300x250+200+200")  # Встановлюємо розміри вікна

    settings.grab_set()  ##################
    settings.focus_set()  # Контроль фокуса вікна
    settings.wait_window()  ##################

    settings.mainloop()


win = Tk()

# Создаємо головне меню
mainmenu = Menu(win)
win.config(menu=mainmenu)

# Создаємо подменю Налаштування
settingsmenu = Menu(mainmenu, tearoff=0)

# Заполнюємо подменю Налаштування
settingsmenu.add_cascade(label="Налаштування фігури", command=image_settings)
settingsmenu.add_cascade(label="Налаштування тексту", command=text_settings)

# Заповнюємо головне меню
mainmenu.add_cascade(label="Налаштування", menu=settingsmenu)

b_triangle = Button(text="Трикутник", width=15, command=triangle)
b_rectangle = Button(text="Прямокутник", width=15, command=rectangle)
# Додаємо кнопку для Кола
b_circle = Button(text="Коло", width=15, command=circle)
# Додаємо кнопку для очищення
b_clear = Button(text="Стерти", width=15, command=clear)
canvas = Canvas(width=400, height=300, bg='#fff')
text = Text(width=55, height=5, bg='#fff', wrap=WORD)
t = canvas.create_polygon(0, 0, 0, 0, 0, 0)
r = canvas.create_rectangle(0, 0, 0, 0)
# Створюємо об'єкт коло
c = canvas.create_oval(0, 0, 0, 0)
print(c)
b_triangle.grid(row=0, column=0)
b_rectangle.grid(row=1, column=0)
# Розміщуємо кнопку "Коло"
b_circle.grid(row=2, column=0)
# Розміщуємо кнопку "Стерти"
b_clear.grid(row=3, column=0)
canvas.grid(row=0, column=1, rowspan=10)
text.grid(row=11, column=1, rowspan=3)

win.mainloop()
