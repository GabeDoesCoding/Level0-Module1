from tkinter import messagebox, simpledialog, Tk



if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    bday = simpledialog.askstring(title='Birthday', prompt ="What is your birthday? (Answer in MM/DD format)")
    if bday == '11/16':
        messagebox.showinfo(title='Unbirthday', message='Have a happy birthday!')
    else:
        messagebox.showinfo(title='Unbirthday', message='Have a very merry UNbirthday')