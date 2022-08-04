import tkinter as tk
import json


def edit():
    if name:
        name.delete(0, tk.END)
    if password:
        password.delete(0, tk.END)


def accept():
    data = {}
    login = name.get()
    passw = password.get()
    data['login'] = login
    data['password'] = passw
    print(f'Login {login}')
    print(f'Password {passw}')
    with open('data.txt', 'a') as fh:
        json.dump(data, fh, ensure_ascii=False)
        win.destroy()


win = tk.Tk()
# заголовок, іконка, фон вікна
win.title('CleanFolder')
photo = tk.PhotoImage(file='win_ico.png')
win.iconphoto(False, photo)
win.config(bg='#404040')

# геометрія вікна
win.geometry('600x500+700+150')
win.minsize(300, 250)
win.maxsize(1200, 1000)
win.resizable(False, False)

# віджет Label
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

# віджет  Buttom

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
# relief=tk.RAISED,
# bd=10,
# justify=tk.RIGHT
# )
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

# Entry віджет Ввід
tk.Label(win, text='Login',  width=10).grid(row=0, column=0)
tk.Label(win, text='Password', width=10).grid(row=1, column=0)
# win.grid_columnconfigure(0, minsize=50)
# win.grid_columnconfigure(1, minsize=50)

name = tk.Entry(win, width=16)
password = tk.Entry(win, width=16, show='*')
name.grid(row=0, column=1)
password.grid(row=1, column=1)

tk.Button(win, text='Edit', command=edit, anchor='center', relief=tk.RAISED, width=6).grid(row=3, column=0, sticky='se')


tk.Button(win, text='Accept', command=accept, anchor='center', width=14).grid(row=3, column=1, sticky='se')

win.mainloop()
