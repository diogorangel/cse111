import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Rectangle Area Calculator")

    # Call function to create the GUI
    populate_main_window(root)

    root.mainloop()

def populate_main_window(root):
    # Create labels and text fields
    lbl_width = ttk.Label(root, text="Width:")
    lbl_height = ttk.Label(root, text="Height:")
    lbl_area = ttk.Label(root, text="Area:")

    txt_width = ttk.Entry(root, width=10)
    txt_height = ttk.Entry(root, width=10)
    lbl_result = ttk.Label(root, text="")
    lbl_status = ttk.Label(root, text="", foreground="red")

    def calculate():
        try:
            width = float(txt_width.get())
            height = float(txt_height.get())
            area = width * height
            lbl_result.config(text=f"{area:.2f}")
            lbl_status.config(text="")  # Clear status if successful
        except ValueError:
            lbl_status.config(text="Please enter valid numbers.")

    def clear():
        txt_width.delete(0, tk.END)
        txt_height.delete(0, tk.END)
        lbl_result.config(text="")
        lbl_status.config(text="")

    # Create buttons
    btn_calc = ttk.Button(root, text="Calculate", command=calculate)
    btn_clear = ttk.Button(root, text="Clear", command=clear)

    # Layout with grid
    lbl_width.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    txt_width.grid(row=0, column=1, padx=5, pady=5)

    lbl_height.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    txt_height.grid(row=1, column=1, padx=5, pady=5)

    lbl_area.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    lbl_result.grid(row=2, column=1, padx=5, pady=5)

    btn_calc.grid(row=3, column=0, padx=5, pady=5)
    btn_clear.grid(row=3, column=1, padx=5, pady=5)

    lbl_status.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="w")

if __name__ == "__main__":
    main()
