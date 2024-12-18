

from owlready2 import *

# Load ontology
onto = get_ontology("c:/Users/Lenevo/Documents/Geomertry1.owx").load()


import tkinter as tk
from tkinter import ttk
from math import pi

def calculate_triangle_area():
    base = float(entry_base.get())
    height = float(entry_height.get())
    area = 0.5 * base * height
    result_label_triangle.config(text=f"Area: {area:.2f} square units")
    formula_label_triangle.config(text="Formula: 0.5 * Base * Height")
    canvas_triangle.delete("all")
    scale = min(200 / base, 200 / height) if base > 0 and height > 0 else 1
    x1, y1 = 20, 180
    x2, y2 = 20 + base * scale, 180
    x3, y3 = 20, 180 - height * scale
    canvas_triangle.create_polygon(x1, y1, x2, y2, x3, y3, fill="lightblue", outline="black")
    canvas_triangle.create_text((x1 + x2) / 2, y1 + 10, text=f"Base: {base} units", font=("Arial", 8))
    canvas_triangle.create_text(x1 - 10, (y1 + y3) / 2, text=f"Height: {height} units", font=("Arial", 8), angle=90)

def calculate_square_area():
    side = float(entry_side.get())
    area = side * side
    result_label_square.config(text=f"Area: {area:.2f} square units")
    formula_label_square.config(text="Formula: Side * Side")
    canvas_square.delete("all")
    scale = 200 / side if side > 0 else 1
    x1, y1 = 20, 20
    x2, y2 = 20 + side * scale, 20 + side * scale
    canvas_square.create_rectangle(x1, y1, x2, y2, fill="lightgreen", outline="black")
    canvas_square.create_text((x1 + x2) / 2, y1 - 10, text=f"Side: {side} units", font=("Arial", 8))

def calculate_circle_area():
    radius = float(entry_radius.get())
    area = pi * radius**2
    result_label_circle.config(text=f"Area: {area:.2f} square units")
    formula_label_circle.config(text="Formula: π * Radius²")
    canvas_circle.delete("all")
    scale = 100 / radius if radius > 0 else 1
    cx, cy = 120, 120
    r = radius * scale
    canvas_circle.create_oval(cx - r, cy - r, cx + r, cy + r, fill="lightcoral", outline="black")
    canvas_circle.create_text(cx, cy + r + 10, text=f"Radius: {radius} units", font=("Arial", 8))

def calculate_rectangle_area():
    length = float(entry_length.get())
    width = float(entry_width.get())
    area = length * width
    result_label_rectangle.config(text=f"Area: {area:.2f} square units")
    formula_label_rectangle.config(text="Formula: Length * Width")
    canvas_rectangle.delete("all")
    scale = min(200 / length, 200 / width) if length > 0 and width > 0 else 1
    x1, y1 = 20, 20
    x2, y2 = 20 + length * scale, 20 + width * scale
    canvas_rectangle.create_rectangle(x1, y1, x2, y2, fill="lightyellow", outline="black")
    canvas_rectangle.create_text((x1 + x2) / 2, y1 - 10, text=f"Length: {length} units", font=("Arial", 8))
    canvas_rectangle.create_text(x2 + 10, (y1 + y2) / 2, text=f"Width: {width} units", font=("Arial", 8), angle=90)

def calculate_rhombus_area():
    d1 = float(entry_d1.get())
    d2 = float(entry_d2.get())
    area = 0.5 * d1 * d2
    result_label_rhombus.config(text=f"Area: {area:.2f} square units")
    formula_label_rhombus.config(text="Formula: 0.5 * D1 * D2")
    canvas_rhombus.delete("all")
    scale = min(200 / d1, 200 / d2) if d1 > 0 and d2 > 0 else 1
    cx, cy = 120, 120
    dx, dy = d1 * scale / 2, d2 * scale / 2
    canvas_rhombus.create_polygon(cx, cy - dy, cx + dx, cy, cx, cy + dy, cx - dx, cy, fill="lightpink", outline="black")
    canvas_rhombus.create_text(cx, cy - dy - 10, text=f"D1: {d1} units", font=("Arial", 8))
    canvas_rhombus.create_text(cx + dx + 10, cy, text=f"D2: {d2} units", font=("Arial", 8))

root = tk.Tk()
root.title("Shape Area Calculator")
root.geometry("400x800")  # Increased height to accommodate larger images
root.configure(bg="#f0f8ff")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Triangle Tab
frame_triangle = tk.Frame(notebook, bg="#e6f7ff")
notebook.add(frame_triangle, text="Triangle")
tk.Label(frame_triangle, text="Triangle Area Calculator", font=("Arial", 12, "bold"), bg="#e6f7ff").pack()
tk.Label(frame_triangle, text="Base:", bg="#e6f7ff", font=("Arial", 10)).pack()
entry_base = tk.Entry(frame_triangle, width=10, font=("Arial", 10))
entry_base.pack()
tk.Label(frame_triangle, text="Height:", bg="#e6f7ff", font=("Arial", 10)).pack()
entry_height = tk.Entry(frame_triangle, width=10, font=("Arial", 10))
entry_height.pack()
tk.Button(frame_triangle, text="Calculate", command=calculate_triangle_area, bg="#80c1ff", fg="white", font=("Arial", 10)).pack(pady=2)
result_label_triangle = tk.Label(frame_triangle, text="", font=("Arial", 10), bg="#e6f7ff")
result_label_triangle.pack()
formula_label_triangle = tk.Label(frame_triangle, text="", font=("Arial", 10), bg="#e6f7ff")
formula_label_triangle.pack()
canvas_triangle = tk.Canvas(frame_triangle, width=240, height=300, bg="white")  # Increased canvas size
canvas_triangle.pack(pady=2)

# Square Tab
frame_square = tk.Frame(notebook, bg="#f0fff0")
notebook.add(frame_square, text="Square")
tk.Label(frame_square, text="Square Area Calculator", font=("Arial", 12, "bold"), bg="#f0fff0").pack()
tk.Label(frame_square, text="Side Length:", bg="#f0fff0", font=("Arial", 10)).pack()
entry_side = tk.Entry(frame_square, width=10, font=("Arial", 10))
entry_side.pack()
tk.Button(frame_square, text="Calculate", command=calculate_square_area, bg="#66cdaa", fg="white", font=("Arial", 10)).pack(pady=2)
result_label_square = tk.Label(frame_square, text="", font=("Arial", 10), bg="#f0fff0")
result_label_square.pack()
formula_label_square = tk.Label(frame_square, text="", font=("Arial", 10), bg="#f0fff0")
formula_label_square.pack()
canvas_square = tk.Canvas(frame_square, width=240, height=300, bg="white")  # Increased canvas size
canvas_square.pack(pady=2)

# Circle Tab
frame_circle = tk.Frame(notebook, bg="#fff0f5")
notebook.add(frame_circle, text="Circle")
tk.Label(frame_circle, text="Circle Area Calculator", font=("Arial", 12, "bold"), bg="#fff0f5").pack()
tk.Label(frame_circle, text="Radius:", bg="#fff0f5", font=("Arial", 10)).pack()
entry_radius = tk.Entry(frame_circle, width=10, font=("Arial", 10))
entry_radius.pack()
tk.Button(frame_circle, text="Calculate", command=calculate_circle_area, bg="#ff69b4", fg="white", font=("Arial", 10)).pack(pady=2)
result_label_circle = tk.Label(frame_circle, text="", font=("Arial", 10), bg="#fff0f5")
result_label_circle.pack()
formula_label_circle = tk.Label(frame_circle, text="", font=("Arial", 10), bg="#fff0f5")
formula_label_circle.pack()
canvas_circle = tk.Canvas(frame_circle, width=240, height=240, bg="white")  # Increased canvas size
canvas_circle.pack(pady=2)

# Rectangle Tab
frame_rectangle = tk.Frame(notebook, bg="#ffffe0")
notebook.add(frame_rectangle, text="Rectangle")
tk.Label(frame_rectangle, text="Rectangle Area Calculator", font=("Arial", 12, "bold"), bg="#ffffe0").pack()
tk.Label(frame_rectangle, text="Length:", bg="#ffffe0", font=("Arial", 10)).pack()
entry_length = tk.Entry(frame_rectangle, width=10, font=("Arial", 10))
entry_length.pack()
tk.Label(frame_rectangle, text="Width:", bg="#ffffe0", font=("Arial", 10)).pack()
entry_width = tk.Entry(frame_rectangle, width=10, font=("Arial", 10))
entry_width.pack()
tk.Button(frame_rectangle, text="Calculate", command=calculate_rectangle_area, bg="#ffd700", fg="black", font=("Arial", 10)).pack(pady=2)
result_label_rectangle = tk.Label(frame_rectangle, text="", font=("Arial", 10), bg="#ffffe0")
result_label_rectangle.pack()
formula_label_rectangle = tk.Label(frame_rectangle, text="", font=("Arial", 10), bg="#ffffe0")
formula_label_rectangle.pack()
canvas_rectangle = tk.Canvas(frame_rectangle, width=240, height=300, bg="white")  # Increased canvas size
canvas_rectangle.pack(pady=2)

# Rhombus Tab
frame_rhombus = tk.Frame(notebook, bg="#ffecf0")
notebook.add(frame_rhombus, text="Rhombus")
tk.Label(frame_rhombus, text="Rhombus Area Calculator", font=("Arial", 12, "bold"), bg="#ffecf0").pack()
tk.Label(frame_rhombus, text="Diagonal 1 (D1):", bg="#ffecf0", font=("Arial", 10)).pack()
entry_d1 = tk.Entry(frame_rhombus, width=10, font=("Arial", 10))
entry_d1.pack()
tk.Label(frame_rhombus, text="Diagonal 2 (D2):", bg="#ffecf0", font=("Arial", 10)).pack()
entry_d2 = tk.Entry(frame_rhombus, width=10, font=("Arial", 10))
entry_d2.pack()
tk.Button(frame_rhombus, text="Calculate", command=calculate_rhombus_area, bg="#ff1493", fg="white", font=("Arial", 10)).pack(pady=2)
result_label_rhombus = tk.Label(frame_rhombus, text="", font=("Arial", 10), bg="#ffecf0")
result_label_rhombus.pack()
formula_label_rhombus = tk.Label(frame_rhombus, text="", font=("Arial", 10), bg="#ffecf0")
formula_label_rhombus.pack()
canvas_rhombus = tk.Canvas(frame_rhombus, width=240, height=300, bg="white")  # Increased canvas size
canvas_rhombus.pack(pady=2)

root.mainloop()
