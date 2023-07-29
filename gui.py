import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar


def get_selected_date():
    selected_date = cal.get_date()
    selected_date_label.config(text=f"Selected Date: {selected_date}")


root = tk.Tk()
root.title("GUI Calendar This is 2nd Projec")
root.geometry("700x600")

cal = Calendar(root, selectmode="day", date_pattern="D/m/y")
cal.pack(pady=10, fill="both", expand=True)
frame = ttk.Frame(root)
frame.pack()

get_date_btn = ttk.Button(frame, text="Get Selected Date : ", command=get_selected_date)
get_date_btn.pack(side="left", padx=10)
quit_btn = ttk.Button(frame, text="Quit_btn", command=root.quit)
quit_btn.pack(side="right", padx=10)
selected_date_label = ttk.Label(root, text="", font=("Helvetica", 14))
selected_date_label.pack(pady=10)
root.mainloop()
