"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
A = 0
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    messagebox.showinfo(title='Riddle', message="You will be asked 3 riddles. At the end of the round, you will know how many you got right out of 3.")
    Q1 = simpledialog.askstring(title='Question 1',prompt="David's father has 3 sons. Snap, Crackle and _____. What is the third son's name?")
    if Q1 == 'David' or Q1 == 'david':
       A = A + 1
    Q2 = simpledialog.askstring(title='Question 2', prompt= "You walk into a cabin and it is pitch black. There is a lantern, a candle and a fireplace. You only have one match. Which do you light first? Answer starts with The, and words are capitalized")
    if Q2 == "The Match":
       A = A + 1
    Q3 = simpledialog.askstring(title='Question 3', prompt="What has roots as nobody sees, is taller than trees, up, up it goes, and yet never grows?")
    if Q3 == "A mountain":
       A = A + 1

    messagebox.showinfo(title='You finished!', message="You got " + str(A) + " correct!")