import tkinter as tk
from tkinter import ttk

win = tk.Tk()
# заголовок, іконка, фон вікна
win.title('tkinter gui')
photo = tk.PhotoImage(file='tkinter/win_ico.png')
win.iconphoto(False, photo)
win.config(bg='#404040')

# геометрія вікна
win.geometry(f'600x800+600+200')
win.minsize(800, 600)
win.maxsize(1200, 1000)
win.resizable(True, True)

''' віджет Label '''
# label_1 = tk.Label(win, text='Clean',
#                    bg='green',
#                    fg='white',
#                    font=('Arial', 15, 'bold'),
#                    padx=20,
#                    pady=20,
#                    width=20,
#                    height=20,
#                    anchor='nw',
#                    relief=tk.RAISED,
#                    bd=10,
#                    justify=tk.RIGHT
#                    )

''' віджет  Buttom '''

# btm_1 = tk.Button(win, text='Clean',
#                   command=main,
#                   activebackground='green',
#                   background='white',
#                   font=('Arial', 15, 'bold'),
#                   padx=30,
#                   pady=10,
#                   width=10,
#                   height=5,
#                   anchor='center',
#                   relief=tk.RAISED,
#                   bd=10,
#                   justify=tk.RIGHT
#                   )
# btm_2 = tk.Button(win, text='Clear',
#                   command=main,
#                   activebackground='green',
#                   background='white',
#                   font=('Arial', 15, 'bold'),
#                   anchor='e'
#                   )
# btm_1.pack()
# btm_2.pack()
#
# btm_3 = tk.Button(win, text='Start',
#                   )
# btm_4 = tk.Button(win, text='Stop',
#                   )
# btm_3.grid(row=0, column=0, sticky='ne')
# btm_4.grid(row=1, column=1, sticky='ne')
# btm_3.columnconfigure(0, minsize=200)
# btm_4.columnconfigure(1, minsize=200)

''' Віджет CheackButtom '''


def select_all():
    for check in [over_18, commercial, follow]:
        check.select()


def deselect_all():
    for check in [over_18, commercial, follow]:
        check.deselect()


def switch_all():
    for check in [over_18, commercial, follow]:
        check.toggle()


def show():
    print(f'Age 18? {over_18_value.get()}')
    print(f'Deal? {commercial_value.get()}')
    print(f'Subscribe {follow_value.get()}')


over_18_value = tk.StringVar()
over_18_value.set('No')
commercial_value = tk.IntVar()
follow_value = tk.BooleanVar()
follow_value.set(False)

over_18 = tk.Checkbutton(win, text='Are you 18 years old?', variable=over_18_value,
                         offvalue='No', onvalue='Yes')
commercial = tk.Checkbutton(win, text='Do you want buy?', variable=commercial_value,
                            offvalue=0, onvalue=1)
follow = tk.Checkbutton(win, text='Do you want subscribe?', indicatoron=0,
                        variable=follow_value, offvalue=False, onvalue=True)

over_18.pack()
commercial.pack()
follow.pack()

tk.Button(text='Choose all', command=select_all).pack()
tk.Button(text='Reset  all', command=deselect_all).pack()
tk.Button(text='Switch all', command=switch_all).pack()
tk.Button(text='Show', command=show).pack()

''' віджет RadioButton '''

level_var = tk.IntVar()
level_text = tk.StringVar()
spec_var = tk.IntVar()
spec_text = tk.StringVar()


def select_level():
    level = level_var.get()
    if level == 1:
        level_text.set('You choose Junior position')
        print('Junior')
    elif level == 2:
        level_text.set('You choose Middle position')
        print('Middle')
    elif level == 3:
        level_text.set('You choose Senior position')
        print('Senior')


def select_spec():
    spec = spec_var.get()
    if spec == 1:
        spec_text.set('You choose Developer')
    elif spec == 2:
        spec_text.set('You choose Tester')
    elif spec == 3:
        spec_text.set('You choose DevOps')


tk.Label(win, text='Choose your position:').pack()

tk.Radiobutton(win, text='Junior', variable=level_var, value=1, command=select_level).pack()
tk.Radiobutton(win, text='Middle', variable=level_var, value=2, command=select_level).pack()
tk.Radiobutton(win, text='Senior', variable=level_var, value=3, command=select_level).pack()

tk.Label(win, textvariable=level_text).pack()

tk.Label(win, text='Choose your specialization:').pack()

tk.Radiobutton(win, text='Developer', variable=spec_var, value=1, command=select_spec).pack()
tk.Radiobutton(win, text='Tester', variable=spec_var, value=2, command=select_spec).pack()
tk.Radiobutton(win, text='DevOps', variable=spec_var, value=3, command=select_spec).pack()

tk.Label(win, textvariable=spec_text).pack()

'''віджет Combobox '''


def show():
    day = combo.get()
    print(f'You choose {day}')


week_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
int_list = [1, 2, 3, 4, 5]
combo = ttk.Combobox(win, values=week_days)
combo_in = ttk.Combobox(win, values=int_list)
combo.current(0)
combo_in.current(0)
combo.pack()
combo_in.pack()


win.mainloop()
