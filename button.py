from tkinter import *

# create widget
root = Tk()


def myClick():
    myLabel = Label(root, text="Hey, What do what me to do?")
    myLabel.pack()


myButton = Button(root, text="Click me", command=myClick, fg="#ffffff", bg="blue")
myButton.pack()

root.mainloop()
