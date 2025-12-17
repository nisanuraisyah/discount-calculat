import tkinter as tk
from tkinter import messagebox

def calculateDiscount():
    try:
        price = float(entry_price.get())
        discount_percent = float(entry_discount.get())
        quantity = int(entry_quantity.get())

        if price < 0 or not (0 <= discount_percent <= 100) or quantity <= 0:
            raise ValueError

        discount_amount = price * (discount_percent / 100)
        final_price = (price - discount_amount) * quantity

        resultLabel.config(
            text=f"Total Price: Rp. {final_price:,.2f}",
            bg="#C8E6C9",
            fg="#1B5E20"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid values:\n"
            "- Price > 0\n"
            "- Discount 0–100%\n"
            "- Quantity > 0"
        )

# ================= WINDOW =================
window = tk.Tk()
window.geometry("450x380")
window.title("Discount Calculator")
window.configure(bg="#E3F2FD")

# ================= TITLE =================
titleLabel = tk.Label(
    window,
    text="\u2B50 Discount Calculator \u2B50",
    font=("Calibri", 18, "bold"),
    bg="#E3F2FD",
    fg="#0D47A1"
)
titleLabel.pack(pady=15)

# ================= FRAME PRICE =================
frame1 = tk.Frame(window, bg="#BBDEFB", bd=2, relief="ridge")
label1 = tk.Label(frame1, text="Price:", bg="#BBDEFB", fg="#0D47A1")
entry_price = tk.Entry(frame1, width=20)

label1.grid(row=0, column=0, padx=10, pady=10)
entry_price.grid(row=0, column=1, padx=10, pady=10)
frame1.pack(pady=5)

# ================= FRAME DISCOUNT =================
frame2 = tk.Frame(window, bg="#C5CAE9", bd=2, relief="ridge")
label2 = tk.Label(frame2, text="Discount (%):", bg="#C5CAE9", fg="#1A237E")
entry_discount = tk.Entry(frame2, width=20)

label2.grid(row=0, column=0, padx=10, pady=10)
entry_discount.grid(row=0, column=1, padx=10, pady=10)
frame2.pack(pady=5)

# ================= FRAME QUANTITY =================
frame3 = tk.Frame(window, bg="#D1C4E9", bd=2, relief="ridge")
label3 = tk.Label(frame3, text="Quantity:", bg="#D1C4E9", fg="#311B92")
entry_quantity = tk.Entry(frame3, width=20)

label3.grid(row=0, column=0, padx=10, pady=10)
entry_quantity.grid(row=0, column=1, padx=10, pady=10)
frame3.pack(pady=5)

# ================= BUTTON =================
button1 = tk.Button(
    window,
    text="Calculate",
    command=calculateDiscount,
    bg="#1976D2",
    fg="white",
    font=("Calibri", 11, "bold"),
    activebackground="#0D47A1",
    activeforeground="white",
    width=15
)
button1.pack(pady=15)

# ================= RESULT =================
resultLabel = tk.Label(
    window,
    text="Total Price: Rp. 0.00",
    font=("Calibri", 13, "bold"),
    bg="#FFF9C4",
    fg="#F57F17",
    relief="sunken",
    padx=20,
    pady=10
)
resultLabel.pack(pady=10)

window.mainloop()
