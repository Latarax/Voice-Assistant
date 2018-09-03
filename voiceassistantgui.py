from tkinter import *
from voiceassistant import loop

root = Tk()

testFrame = Frame(root)

triggerButton = Button(testFrame, text="Voice Assistant", width=25, height=10)

triggerButton.bind("<Button-1>", loop)

root.geometry("500x500")
testFrame.pack()
triggerButton.grid(row=1, column=2)



root.mainloop()