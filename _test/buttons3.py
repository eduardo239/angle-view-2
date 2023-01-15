from tkinter import *

root = Tk()

listbox = Listbox(root)

# fill option added to make widget fill entire frame.
# expand option added to expand widget, if user resizes frame.
listbox.pack(fill=BOTH, expand=1)

for z in range(4):
    listbox.insert(END, str(z))

mainloop()
