import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    Joe = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    Shape = simpledialog.askstring(title='Shape',prompt="What shape do you want to draw?")
    # Draw the shape requested by the user using if-elif-else statements
    
    # Call the turtle .done() method
