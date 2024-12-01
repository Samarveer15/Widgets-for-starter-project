import tkinter as tk
from tkinter import ttk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, str(product))
    except ValueError:
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, "Please enter valid numbers")

root = tk.Tk()
root.geometry("400x300")
root.title("Getting Started with Widgets")

description_label = ttk.Label(root, text="This application calculates the product of two numbers.")
description_label.pack(pady=10)

label1 = ttk.Label(root, text="Enter the first number:")
label1.pack()
entry1 = ttk.Entry(root)
entry1.pack()

label2 = ttk.Label(root, text="Enter the second number:")
label2.pack()
entry2 = ttk.Entry(root)
entry2.pack()

calculate_button = ttk.Button(root, text="Calculate", command=calculate_product)
calculate_button.pack(pady=10)

result_textbox = tk.Text(root, height=1, width=20)
result_textbox.pack()

root.mainloop()
