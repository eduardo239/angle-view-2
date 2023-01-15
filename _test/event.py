import tkinter as tk

window = tk.Tk()


def handle_keypress(event):
    print(event.char)


def handle_click(event):
    print(event)


button = tk.Button(text="click")
button.pack()

window.bind("<Key>", handle_keypress)
window.bind("<Button-1>", handle_click)
# <Button-2><Button-3>
window.mainloop()
