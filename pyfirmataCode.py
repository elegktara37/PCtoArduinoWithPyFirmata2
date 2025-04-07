from tkinter import *
from tkinter import ttk
import pyfirmata2
from pyfirmata2 import Arduino, util, STRING_DATA

port = 'COM3'
board = pyfirmata2.Arduino(port)

#Arduino.AUTODETECT

root = Tk()
root.title("Firmata Arduino Controller")
root.geometry("400x150")

def displayFirstName():
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("John"))
def displayLastName():
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter("Snow"))

ttk.Button(root, text="Display First Name", width=20, command=displayFirstName).grid(row=1, column=0, ipadx=10, ipady=10)
ttk.Button(root, text="Display Last Name", width=20, command=displayLastName).grid(row=1, column=1, ipadx=10, ipady=10)

root.mainloop()

# Don't forget to close board on exit (optional but clean)
board.exit()
