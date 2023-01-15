import tkinter as tk
from PIL import ImageTk, Image
from functions import *
from ImageFile import ImageFile

s = ImageFile()
start(s)

bg = "#2d2d2d"
rg = "#1D1D1D"
pp = "#7305FF"
wh = "#ffffff"

root = tk.Tk()
root.title("Angle View")
root.configure(bg=bg)
root.resizable(width=False, height=False)

window_width = 500
window_height = 250

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

position_bottom = screen_height - window_height - 32
position_right = screen_width - window_width

# root.eval('tk::PlaceWindow . center')
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_bottom}')

pixel = tk.PhotoImage(width=1, height=1)

left_frame = tk.Frame(root, width=250, height=250, bg=bg)
right_frame = tk.Frame(root, width=250, height=250, bg=bg)

left_frame.grid(row=0, column=0, padx=0, pady=0)
right_frame.grid(row=0, column=1, padx=0, pady=0, sticky="n")

image = Image.open(FILENAME)
image = image.resize((250, 250))
screenshot = ImageTk.PhotoImage(image)
label_screenshot = tk.Label(image=screenshot, bg=bg)
label_screenshot.image = screenshot
label_screenshot.place(x=0, y=0)

cos = tk.Frame(right_frame, width=250, height=40, bg=rg)
sin = tk.Frame(right_frame, width=250, height=40, bg=rg)
res = tk.Frame(right_frame, width=250, height=40, bg=rg)
buttons = tk.Frame(right_frame, width=250, height=40, bg=pp)

cos.grid(row=0, column=0)
sin.grid(row=1, column=0)
res.grid(row=2, column=0)

label_cos = tk.Label(cos, text="0.00000", font='"monospace" 15', width=20, anchor="w", bg=rg, fg=wh)
label_sin = tk.Label(sin, text="0.00000", font='"monospace" 15', width=20, anchor="w", bg=rg, fg=wh)
label_res = tk.Label(res, text="0.00000", font='"monospace" 15', width=20, anchor="w", bg=rg, fg=wh)

label_cos.grid(row=0, column=0)
label_sin.grid(row=0, column=1)
label_res.grid(row=0, column=2)

root.bind("<Button-1>", lambda e: handle_click(e, label_cos, label_sin, label_res, left_frame))
root.bind("<Key>", lambda e: handle_keypress(e, s))

buttons.grid(row=3, column=0, sticky='ew')

button_frame = tk.Frame(buttons, bg=rg)

button_update = tk.Button(button_frame,
                          text="Update",
                          command=lambda: update(s),
                          width=83,
                          height=40,
                          bg=pp,
                          fg=wh,
                          relief="flat",
                          borderwidth=0,
                          compound="c",
                          image=pixel
                          )
button_auto = tk.Button(button_frame,
                        text="Auto",
                        command=lambda: auto(s),
                        width=83,
                        height=40,
                        bg=pp,
                        fg=wh,
                        relief="flat",
                        borderwidth=0,
                        compound="c",
                        image=pixel
                        )
button_folder = tk.Button(button_frame,
                          text="Folder",
                          command=lambda: folder(s),
                          width=83,
                          height=40,
                          bg=pp,
                          fg=wh,
                          relief="flat",
                          borderwidth=0,
                          compound="c",
                          image=pixel
                          )

plus = tk.Button(button_frame, text="Ruler",
                 command=lambda: window_ruler(root),
                 bg=pp,
                 fg=wh,
                 relief="flat",
                 )
minus = tk.Button(button_frame, text="Close Ruler",
                  
                  bg=pp,
                  fg=wh,
                  relief="flat",
                  )

button_update.grid(row=0, column=0)
button_auto.grid(row=0, column=1)
button_folder.grid(row=0, column=2)
plus.grid(row=1, column=0, columnspan=3, sticky='ew')
minus.grid(row=2, column=0, columnspan=3, sticky='ew')

button_frame.pack(expand=True, fill='both')

root.mainloop()
