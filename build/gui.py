from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"/Users/jeanieho/Documents/DataHack/build/assets/frame0"
)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Amazon Review Bot or Not")
window.geometry("524x691")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=691,
    width=524,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(262.0, 345.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(273.54193115234375, 628.306884765625, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(155.0, 626.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(161.0, 628.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(263.0, 74.0, image=image_image_5)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(262.0, 297.0, image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(434.0, 165.0, image=image_image_7)

image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(101.0, 531.0, image=image_image_8)

image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(101.0, 536.0, image=image_image_9)

image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(124.0, 75.0, image=image_image_10)

image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(186.0, 75.0, image=image_image_11)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(261.0, 325.5, image=entry_image_1)
entry_1 = Text(bd=0, bg="#000000", fg="#FFFFFF", highlightthickness=0, wrap="word")
entry_1.place(x=82.0, y=200.0, width=358.0, height=249.0)


# function to display user text when
# button is clicked
def clicked():
    user_input = entry_1.get("1.0", "end-1c")  # get the text input from the Text widget
    # for example:
    # if "This is a fake review" in user_input:
    #     message = "This is a fake review."
    # else:
    #     message = "This is a genuine review."
    # update the canvas with the result
    message = f"You wrote: {user_input}"
    entry_1.delete("1.0", "end")  # delete the existing text
    entry_1.insert("1.0", message)  # insert the new message


button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=clicked,
    relief="flat",
)
button_1.place(x=314.0, y=506.0, width=160.0, height=60.0)

image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(286.0, 75.0, image=image_image_12)

image_image_13 = PhotoImage(file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(239.0, 75.0, image=image_image_13)

image_image_14 = PhotoImage(file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(344.0, 75.0, image=image_image_14)

image_image_15 = PhotoImage(file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(391.0, 75.0, image=image_image_15)

image_image_16 = PhotoImage(file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(439.0, 75.0, image=image_image_16)

image_image_17 = PhotoImage(file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(196.0, 152.0, image=image_image_17)

image_image_18 = PhotoImage(file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(212.0, 172.0, image=image_image_18)

image_image_19 = PhotoImage(file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(226.0, 152.0, image=image_image_19)

image_image_20 = PhotoImage(file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(90.0, 168.0, image=image_image_20)

image_image_21 = PhotoImage(file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(124.0, 168.0, image=image_image_21)

image_image_22 = PhotoImage(file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(214.0, 168.0, image=image_image_22)

image_image_23 = PhotoImage(file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(167.0, 168.0, image=image_image_23)

image_image_24 = PhotoImage(file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(259.0, 169.0, image=image_image_24)

canvas.create_rectangle(313.0, 505.0, 474.0, 506.0, fill="#000000", outline="")
window.resizable(False, False)
window.mainloop()
