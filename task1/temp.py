import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        value = float(entry_value.get())
        unit = variable.get()
        
        if unit == 'C':
            fahrenheit = celsius_to_fahrenheit(value)
            kelvin = celsius_to_kelvin(value)
            result_label.config(text=f"{value}°C = {fahrenheit:.2f}°F, {kelvin:.2f}K")
        elif unit == 'F':
            celsius = fahrenheit_to_celsius(value)
            kelvin = fahrenheit_to_kelvin(value)
            result_label.config(text=f"{value}°F = {celsius:.2f}°C, {kelvin:.2f}K")
        elif unit == 'K':
            celsius = kelvin_to_celsius(value)
            fahrenheit = kelvin_to_fahrenheit(value)
            result_label.config(text=f"{value}K = {celsius:.2f}°C, {fahrenheit:.2f}°F")
        else:
            result_label.config(text="Please select a valid unit.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric value for the temperature.")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("420x320")
root.configure(bg='#1e1e2d')  # Dark background

# Styles
label_style = {'font': ('Helvetica', 12), 'bg': '#1e1e2d', 'fg': 'white'}  # White text on dark background
entry_style = {'font': ('Helvetica', 12), 'width': 10, 'bg': '#33334d', 'fg': 'white', 'insertbackground': 'white'}  # Styled entry box
button_style = {'font': ('Helvetica', 12), 'width': 10, 'bg': '#007acc', 'fg': 'white', 'activebackground': '#005999', 'bd': 0}  # Styled button
result_style = {'font': ('Helvetica', 12), 'fg': '#00e676', 'bg': '#1e1e2d'}  # Bright result text

# Frame to center content
content_frame = tk.Frame(root, bg='#1e1e2d')
content_frame.pack(expand=True, anchor='center')

# Widgets inside the frame
tk.Label(content_frame, text="Temperature Converter", **label_style).pack(pady=15)
tk.Label(content_frame, text="Enter Temperature Value:", **label_style).pack(pady=5)
entry_value = tk.Entry(content_frame, **entry_style)
entry_value.pack(pady=5)

tk.Label(content_frame, text="Select Unit whether celcius or fahrenheit or kelvin:", **label_style).pack(pady=5)
variable = tk.StringVar(root)
variable.set("C")  # default value
units_menu = tk.OptionMenu(content_frame, variable, "C", "F", "K")
units_menu.config(bg='#33334d', fg='white', font=('Helvetica', 12), bd=0, highlightthickness=0, activebackground='#444466')
units_menu.pack(pady=5)

convert_button = tk.Button(content_frame, text="Convert", command=convert_temperature, **button_style)
convert_button.pack(pady=20)

result_label = tk.Label(content_frame, text="", **result_style)
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
