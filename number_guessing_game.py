#NUMBER GUESSSING GAME  
import random
import tkinter
from tkinter import *

top =tkinter.Tk()
top.mainloop()

guess = input("Rate die Zahl zwischen 1 und 10: ")
to_guess = random.randint(1,10)

if(guess==to_guess):
    print("WOW CORRECT COOL")
else:
    print("Womp Womp lutsch eier, die richtige Zahl wäre", to_guess)

