from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('600x300')
ws.config(bg='#F2B33D')

frame = Frame(ws, bg='#F2B33D')

Button(frame, text="These buttons").grid(row=0, column=0)
Button(frame, text="are positioned").grid(row=0, column=1)
Button(frame, text="using Grid").grid(row=0, column=2)

Button(frame, text="This is ").grid(row=1, column=0, sticky='ew')
Button(frame, text="another line").grid(row=1, column=1, sticky='ew')
Button(frame, text="using Grid").grid(row=1, column=2)

frame.pack(expand=True)

ws.mainloop()
