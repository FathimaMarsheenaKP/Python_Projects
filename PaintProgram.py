import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import PhotoImage

# prev_x, prev_y = None
current_color = 'black'

def start_dwg(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y
    # print(prev_x, prev_y)

def paint(event):
    global prev_x, prev_y
    x, y = event.x, event.y
    if prev_x and prev_y:
        canvas.create_line(prev_x, prev_y, x, y, fill = current_color, width = 2)
    prev_x, prev_y = x, y

def choose_color():
    global current_color
    color = askcolor()[1]
    if color:
        current_color = color

def clear_canvas():
    canvas.delete('all')


window = tk.Tk()
window.title("Paint Program")

btn_frame = tk.Frame(window)
btn_frame.pack(padx = 5, pady = 5)

color_icon = PhotoImage(file = './static/icons8-color-16.png')
color_btn = tk.Button(btn_frame, text = 'Select Color', font = 'Arial 15', image = color_icon, command = choose_color)
color_btn.grid(row = 0, column = 0, padx = 5)

clear_icon = PhotoImage(file = './static/icons8-clear-48.png')
clear_btn = tk.Button(btn_frame, text = 'Clear', font = 'Arial 15', image = clear_icon, command = clear_canvas)
clear_btn.grid(row = 0, column = 1, padx = 5)

exit_icon = PhotoImage(file = './static/icons8-exit-94.png')
exit_btn = tk.Button(btn_frame, text = 'Exit', font = 'Arial 15', image = exit_icon, command = window.quit)
exit_btn.grid(row = 0, column = 2, padx = 5)

canvas = tk.Canvas(window, bg = 'white', width = 900, height = 600)
canvas.pack(padx = 5, pady = 5)

canvas.bind("<Button-1>", start_dwg)
canvas.bind('<B1-Motion>', paint)



window.mainloop()