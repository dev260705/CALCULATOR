import tkinter as tk
from tkinter import *
from tkinter import messagebox

def on_click(button_text):
    """Handle button clicks"""
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == "C":
        entry.delete(0, END)
    else:
        entry.insert(END, button_text)

def create_rounded_button(canvas, text, x, y, width, height, command, color="#e0e0e0", text_color="black"):
    """Create a rounded button using canvas shapes"""
    radius = height // 2
    id1 = canvas.create_oval(x, y, x + height, y + height, fill=color, outline=color)
    id2 = canvas.create_oval(x + width - height, y, x + width, y + height, fill=color, outline=color)
    id3 = canvas.create_rectangle(x + radius, y, x + width - radius, y + height, fill=color, outline=color)
    
   
    button = canvas.create_text(
        x + width // 2, y + height // 2, text=text, font=("Arial", 14, "bold"), fill=text_color
    )
    
    
    canvas.tag_bind(button, "<Button-1>", lambda e: command())
    canvas.tag_bind(id1, "<Button-1>", lambda e: command())
    canvas.tag_bind(id2, "<Button-1>", lambda e: command())
    canvas.tag_bind(id3, "<Button-1>", lambda e: command())

    return button

def add_buttons(canvas):
    """Add calculator buttons to the canvas"""
    
    buttons = [
        ("7", 30, 100), ("8", 110, 100), ("9", 190, 100), ("/", 270, 100),
        ("4", 30, 180), ("5", 110, 180), ("6", 190, 180), ("*", 270, 180),
        ("1", 30, 260), ("2", 110, 260), ("3", 190, 260), ("-", 270, 260),
        ("0", 30, 340), ("C", 110, 340), ("=", 190, 340), ("+", 270, 340),
    ]

    
    for text, x, y in buttons:
        color = "#4d94ff" if text == "=" else "#f0f0f0" 
        text_color = "white" if text == "=" else "black"
        create_rounded_button(
            canvas, text, x, y, width=70, height=50, 
            command=lambda t=text: on_click(t), 
            color=color, text_color=text_color
        )


root = tk.Tk()
root.title("Calculator")
root.geometry("350x450")
root.resizable(False, False)

canvas = Canvas(root, width=350, height=450, bg="black")
canvas.pack()

entry = Entry(root, font=("Arial", 20), bd=10, relief=GROOVE, justify=RIGHT)
entry.place(x=10, y=20, width=330, height=50)

add_buttons(canvas)

root.mainloop()
