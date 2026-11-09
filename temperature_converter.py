"""Beginner-friendly temperature converter using Python's built-in Tkinter."""

import tkinter as tk
from tkinter import ttk, messagebox


def convert_temperature(value, direction):
    """Return (converted temperature, unit, formula, worked calculation)."""
    if direction == "Celsius to Fahrenheit":
        converted = (value * 9 / 5) + 32
        unit = "°F"
        formula = "°F = (°C × 9/5) + 32"
        calculation = f"({value:g} × 9/5) + 32 = {converted:.2f} °F"
    else:
        converted = (value - 32) * 5 / 9
        unit = "°C"
        formula = "°C = (°F − 32) × 5/9"
        calculation = f"({value:g} − 32) × 5/9 = {converted:.2f} °C"

    return converted, unit, formula, calculation


def main():
    # 1. Create the window and set its appearance.
    window = tk.Tk()
    window.title("Temperature Converter")
    window.geometry("460x430")
    window.minsize(390, 400)
    window.configure(bg="#f1f5f9")

    style = ttk.Style(window)
    style.theme_use("clam")
    style.configure("TFrame", background="white")
    style.configure("TLabel", background="white", foreground="#1f2937", font=("Arial", 11))
    style.configure("TEntry", padding=9)
    style.configure("TCombobox", padding=8)
    style.configure("Convert.TButton", font=("Arial", 11, "bold"), padding=12,
                    background="#4f46e5", foreground="white")
    style.map("Convert.TButton", background=[("active", "#4338ca")],
              foreground=[("active", "white")])

    # 2. Put all controls inside a padded white panel.
    panel = ttk.Frame(window, padding=28)
    panel.pack(fill="both", expand=True, padx=22, pady=22)
    panel.columnconfigure(0, weight=1)

    ttk.Label(panel, text="Temperature Converter",
              font=("Arial", 20, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 8))
    ttk.Label(panel, text="Enter a temperature, then click Convert.",
              foreground="#64748b").grid(row=1, column=0, sticky="w", pady=(0, 22))

    # 3. Input: a field where the user types a number.
    ttk.Label(panel, text="Temperature").grid(row=2, column=0, sticky="w")
    temperature_entry = ttk.Entry(panel, font=("Arial", 13))
    temperature_entry.grid(row=3, column=0, sticky="ew", pady=(6, 16))
    temperature_entry.insert(0, "25")

    # 4. Dropdown: lets the user choose either direction.
    ttk.Label(panel, text="Conversion type").grid(row=4, column=0, sticky="w")
    direction = tk.StringVar(value="Celsius to Fahrenheit")
    direction_dropdown = ttk.Combobox(
        panel, textvariable=direction, state="readonly",
        values=("Celsius to Fahrenheit", "Fahrenheit to Celsius")
    )
    direction_dropdown.grid(row=5, column=0, sticky="ew", pady=(6, 16))

    # 5. Text that will actually change when Convert is clicked.
    result_text = tk.StringVar(value="Your result will appear here")
    formula_text = tk.StringVar(value="")
    calculation_text = tk.StringVar(value="")

    def on_convert():
        """Get the input, calculate the answer, and update the screen."""
        try:
            value = float(temperature_entry.get())
            if not (-float("inf") < value < float("inf")):
                raise ValueError("Temperature must be finite")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number, such as 25 or -10.")
            return

        converted, unit, formula, calculation = convert_temperature(value, direction.get())
        result_text.set(f"{converted:.2f} {unit}")
        formula_text.set(f"Formula: {formula}")
        calculation_text.set(f"Calculation: {calculation}")

    # 6. Convert button; command=on_convert makes it work when clicked.
    ttk.Button(panel, text="Convert", style="Convert.TButton",
               command=on_convert).grid(row=6, column=0, sticky="ew", pady=(0, 22))

    # 7. Result, formula, and step-by-step calculation.
    ttk.Label(panel, text="Converted temperature",
              foreground="#64748b").grid(row=7, column=0, sticky="w")
    ttk.Label(panel, textvariable=result_text,
              font=("Arial", 23, "bold")).grid(row=8, column=0, sticky="w", pady=(4, 12))
    ttk.Label(panel, textvariable=formula_text,
              font=("Arial", 10, "bold")).grid(row=9, column=0, sticky="w", pady=(0, 5))
    ttk.Label(panel, textvariable=calculation_text,
              font=("Arial", 10)).grid(row=10, column=0, sticky="w")

    # Bonus: pressing Enter also converts the temperature.
    window.bind("<Return>", lambda event: on_convert())
    temperature_entry.focus_set()

    # 8. Start the app and keep the window open.
    window.mainloop()


if __name__ == "__main__":
    main()
