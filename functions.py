import math
import os
import tkinter as tk
import cv2
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image

FILENAME = "_screenshot.jpg"
SETTINGS = "settings.txt"

bg = "#2d2d2d"
rg = "#1D1D1D"
pp = "#7305FF"


def load_settings(s):
    try:
        f = open(SETTINGS, 'r')
        s.folder_path = f.read()

    except Exception as e:
        print("load_settings.error")
        print(str(e))
        f = open(SETTINGS, 'w+')
    finally:
        f.close()


def load_file(s):
    try:
        images = []
        if s.folder_path == "" or s.folder_path is None:
            load_settings(s)
        for f in os.listdir(s.folder_path):
            name, ext = os.path.splitext(f)
            if ext == '.jpg' or ext == '.png' or ext == '.jpeg':
                images.append(name + ext)

        s.last_file = images[-1]
    except Exception as e:
        print("load_files.error")
        print(str(e))


def reload_image():
    image = Image.open(FILENAME)
    image = image.resize((250, 250))
    screenshot = ImageTk.PhotoImage(image)
    label_screenshot = tk.Label(image=screenshot, bg=bg)
    label_screenshot.image = screenshot
    label_screenshot.place(x=0, y=0)


def set_cropped_image(s):
    try:
        f = open(FILENAME, 'r')
    except Exception as e:
        print(str(e))
        f = open(SETTINGS, 'w+')


def crop_image(s):
    try:
        full_path = f"{s.folder_path}/{s.last_file}"
        image = cv2.imread(full_path, cv2.IMREAD_COLOR)

        # w 675 x + 34
        # h 475 y + 26
        h, w, _ = image.shape
        y = int(h) - 15
        x = int(w) - 7

        # h - 125, w - 125
        s = 125
        cropped_image = image[h - s + 26:y, w - s + 34:x]
        zoom_cropped_image = cv2.resize(cropped_image, None, fx=2, fy=2)
        cv2.imwrite(FILENAME, zoom_cropped_image)

    except Exception as e:
        print('crop_image.error')
        print(str(e))


def start(s):
    load_settings(s)
    load_file(s)


def update(s):
    load_file(s)
    crop_image(s)
    reload_image()


def handle_keypress(event, s):
    key = event.char

    if key == "w" or key == "u" or key == " ":
        update(s)
    elif key == "a":
        auto(s)


def auto(s):
    pass


def folder(s):
    file_settings = 'settings.txt'
    file_path = askopenfilename(filetypes=[("Text Files", "*.jpg"), ("All Files", "*.*")])
    folder_path = os.path.dirname(file_path)

    try:
        f = open(file_settings, 'w')
    except Exception as e:
        print(str(e))
        f = open(file_settings, 'w')
    finally:
        f.write(folder_path)
        s.folder_path = folder_path
        f.close()


def handle_click(event, label_cos, label_sin, label_res, frame):
    x = event.x
    y = event.y

    draw_dot(frame, x, y)

    width = 250 / 2 + 2
    height = 250 / 2 + 5

    x_distance = abs(int(x - width))
    y_distance = abs(int(y - height))

    distance = math.sqrt(x_distance ** 2 + y_distance ** 2)

    cos = round((x_distance / distance), 5)
    sin = round((y_distance / distance), 5)
    tan = 0 if x_distance == 0 else y_distance / x_distance

    angle = round(abs(math.degrees(math.atan(tan)) - 90), 5)

    label_cos["text"] = f"{cos}"
    label_sin["text"] = f"{sin}"
    label_res["text"] = f"{angle}"


def draw_dot(frame, x, y):
    pass


def window_ruler(root):
    w_ruler = tk.Toplevel(root)
    w_ruler.title("Ruler")
    w_ruler.attributes('-topmost', True, '-alpha', .25, "-transparentcolor", "white")
    w_ruler.overrideredirect(True)

    screen_width = w_ruler.winfo_screenwidth()
    screen_height = w_ruler.winfo_screenheight()

    w_ruler.geometry(f"{screen_width}x30+0+{int(screen_height / 2) - 100}")

    canvas = tk.Canvas(w_ruler, height=30, bg="black")

    for i in range(round(screen_width / 5)):
        fix = 9
        space = 248 / 10
        height = 30
        by_five = i % 5 == 0
        diff = i * space + height + fix

        if by_five:
            canvas.create_line(
                diff,
                0,
                diff,
                height,
                fill='red',
                width=1
            )
        else:
            canvas.create_line(
                diff,
                0,
                diff,
                height,
                fill='green',
                width=1
            )

    canvas.pack(fill='both', expand=True)
