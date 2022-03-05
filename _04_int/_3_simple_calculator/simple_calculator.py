"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    Calculate = simpledialog.askinteger(title="Simple calculator",prompt="Which calculator function would you like to use? Type 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division.")
    if Calculate == 1:
        AddNum1 = simpledialog.askinteger(title='Simple Adder', prompt="Enter in the first number you want to add")
        AddNum2 = simpledialog.askinteger(title='Simple Adder', prompt="Enter in the second number you want to add")
        Ans = AddNum1 + AddNum2
        messagebox.showinfo(title='Simple Adder', message="The answer is "+ str(Ans) +"!")
