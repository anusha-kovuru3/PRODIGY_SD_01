import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature():
    try:
        temp = float(entry_temperature.get())
        unit = selected_unit.get()

        if unit == "Celsius":
            fahrenheit = celsius_to_fahrenheit(temp)
            kelvin = celsius_to_kelvin(temp)
            result_label.config(text=f"Fahrenheit: {fahrenheit:.2f} \u00b0F\nKelvin: {kelvin:.2f} K")
        elif unit == "Fahrenheit":
            celsius = fahrenheit_to_celsius(temp)
            kelvin = fahrenheit_to_kelvin(temp)
            result_label.config(text=f"Celsius: {celsius:.2f} \u00b0C\nKelvin: {kelvin:.2f} K")
        elif unit == "Kelvin":
            celsius = kelvin_to_celsius(temp)
            fahrenheit = kelvin_to_fahrenheit(temp)
            result_label.config(text=f"Celsius: {celsius:.2f} \u00b0C\nFahrenheit: {fahrenheit:.2f} \u00b0F")
        else:
            messagebox.showerror("Error", "Please select a valid unit.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid temperature value.")

root = tk.Tk()
root.title("Temperature Conversion")
root.geometry("400x300")

tk.Label(root, text="Enter Temperature:", font=("Arial", 12)).pack(pady=10)
entry_temperature = tk.Entry(root, font=("Arial", 12))
entry_temperature.pack(pady=5)

selected_unit = tk.StringVar(value="Celsius")
tk.Label(root, text="Select Unit:", font=("Arial", 12)).pack(pady=10)
units_dropdown = tk.OptionMenu(root, selected_unit, "Celsius", "Fahrenheit", "Kelvin")
units_dropdown.pack(pady=5)

tk.Button(root, text="Convert", font=("Arial", 12), command=convert_temperature).pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
