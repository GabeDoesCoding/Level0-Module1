"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    messagebox.showinfo(title='Riddle', message="You will be asked 3 riddles. At the end of the round, you will know how many you got right out of 3.")
    Q1 = simpledialog.askstring(title='Question 1',prompt="David's father has 3 sons. Snap, Crackle and _____. What is the third son's name?")
    if Q1 == 'David' or Q1 == 'david':
