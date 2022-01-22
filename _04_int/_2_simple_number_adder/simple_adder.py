"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    Num1 = simpledialog.askinteger(title='Simple Adder', prompt="Enter in the first number you want to add")
    Num2 = simpledialog.askinteger(title='Simple Adder', prompt="Enter in the second number you want to add")