import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE
}

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="frame a")
label_a.pack()

label_b = tk.Label(master=frame_b, text="frame b")
label_b.pack()

frame_a.pack()
frame_b.pack()

# types
for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()


# tk.FLAT: Has no border effect (the default value)
# tk.SUNKEN: Creates a sunken effect
# tk.RAISED: Creates a raised effect
# tk.GROOVE: Creates a grooved border effect
# tk.RIDGE: Creates a ridged effect
