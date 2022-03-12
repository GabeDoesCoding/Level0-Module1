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
        AddNum1 = simpledialog.askfloat(title='Simple Addition', prompt="Enter in the first number you want to add.")
        AddNum2 = simpledialog.askfloat(title='Simple Addition', prompt="Enter in the second number you want to add.")
        AddAns = AddNum1 + AddNum2
        messagebox.showinfo(title='Simple Addition', message="The answer is "+ str(AddAns) +"!")
    elif Calculate == 2:
        SubNum1 = simpledialog.askfloat(title='Simple Subtraction', prompt="Enter in the first number you want to subtract.")
        SubNum2 = simpledialog.askfloat(title='Simple Subtraction', prompt="Enter in the second number you want to subtract.")
        SubAns = SubNum1 - SubNum2
        messagebox.showinfo(title='Simple Subtraction', message="The answer is " + str(SubAns) +"!")
    elif Calculate == 3:
        MultNum1 = simpledialog.askfloat(title='Simple Multiplication', prompt="What is the first number you want to multiply?")
        MultNum2 = simpledialog.askfloat(title='Simple Multiplication', prompt="What is the second number you want to multiply?")
        MultAns = MultNum1 * MultNum2
        messagebox.showinfo(title='Simple Multiplication', message=" The answer is " +str(MultAns) +"!")
    elif Calculate == 4:
        DivNum1 = simpledialog.askfloat(title='Simple Division', prompt="What is the first number you want to divide?")
        DivNum2 = simpledialog.askfloat(title='Simple Division', prompt="What is the second number you want to divide?")
        DivAns = DivNum1 / DivNum2
        messagebox.showinfo(title='Simple Division', message="The answer is " +str(DivAns) +"!")