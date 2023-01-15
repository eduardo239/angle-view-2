from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#F2B33D')

frame = Frame(ws, bg='#F2B33D')

Button(frame, text="These buttons").grid(row=0, column=0)
Button(frame, text="are positioned").grid(row=0, column=1)
Button(frame, text="using Grid").grid(row=0, column=2)

Button(frame, text="another line").grid(row=1, columnspan=3, sticky='ew')

frame.pack(expand=True)

ws.mainloop()