# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
from tkinter import Tk, messagebox, simpledialog
window = Tk()
window.withdraw


if __name__ == '__main__':


    simpledialog.askstring(title='Circle Calculator', prompt="What is the radius of a circle?")