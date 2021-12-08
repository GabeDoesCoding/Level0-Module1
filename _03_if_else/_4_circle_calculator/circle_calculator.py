# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
import math
from tkinter import Tk, messagebox, simpledialog
window = Tk()
window.withdraw()


if __name__ == '__main__':


    CircRad = simpledialog.askinteger(title='Circle Calculator', prompt="What is the radius of a circle?")
    Choice = simpledialog.askstring(title='Circle Calculator', prompt="Would you like to know the area or the circumference of this circle?")
    if Choice == 'Area' or Choice == 'area':
        messagebox.showinfo(title='Area', message="The area of the circle you entered is " +str(math.pi * (CircRad * CircRad)))

    elif Choice == 'Circumference' or Choice == 'circumference':
        messagebox.showinfo(title='Circumference', message="The circumference of the circle you entered is " +str(CircRad*2*math.pi))
