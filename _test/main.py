import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

greeting = tk.Label(
    text="hello",
    foreground="Pink",
    background="black",
    width=20,
    height=10)
greeting.pack()

button = tk.Button(
    text="click",
    width=8,
    height=5,
    bg="blue",
    fg="yellow"
)

button.pack()

entry = tk.Entry(fg="gray", width=30)
# The interesting bit about Entry widgets isn’t how to style them, though. It’s how to use them to get input from a
# user. There are three main operations that you can perform with Entry widgets: Retrieving text with .get() Deleting
# text with .delete() Inserting text with .insert()

entry.pack()

username = entry.get()
print(username)
# entry.delete(0)
# entry.delete(0, 7)
# entry.delete(0, tk.END)
# entry.delete(0, "Python")
# delete o primeiro caractere

entry.insert(0, "Real ")

text_box = tk.Text()
text_box.focus()
text_box.insert(tk.END, "\nHellow ")
text_box.pack()

user_text = text_box.get("1.0", tk.END)

window.mainloop()

# window.destroy()

