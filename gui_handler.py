import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import bvg_api_handler as bvg


def submit_click():
    arrival_time = arrival_time_value.get()
    prep_time = prep_time_value.get()
    start_point = start_point_value.get()
    destination = destination_value.get()
    travel_time = bvg.get_travel_time(start_point, destination)
    calculate_wake_time(arrival_time, prep_time, travel_time)
    


# create Window
root = tk.Tk()  
root.geometry("300x500")
root.resizable(False, False)
root.title("WakeApp")


arrival_time_value = tk.StringVar(value="00:00")
prep_time_value = tk.StringVar(value="00:00")
start_point_value = tk.StringVar(value="")
destination_value = tk.StringVar(value="")


# frame for time input
input_frame = ttk.Frame(root)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)


# time of arrival input
arrival_label = ttk.Label(input_frame, text="Ankuftszeit (HH:MM): ")
arrival_label.pack(fill="x", expand=True)

arrival_entry = ttk.Entry(input_frame, textvariable=arrival_time_value)
arrival_entry.pack(fill="x", expand=True)


# time to get ready input
prep_label = ttk.Label(input_frame, text="Benötigte Zeit zum fertig zu machen (HH:MM): ")
prep_label.pack(fill="x", expand=True)

prep_entry = ttk.Entry(input_frame, textvariable=prep_time_value)
prep_entry.pack(fill="x", expand=True)


# start point input
start_label = ttk.Label(input_frame, text="Wohnort: ")
start_label.pack(fill="x", expand=True)

start_entry = ttk.Entry(input_frame, textvariable=start_point_value)
start_entry.pack(fill="x", expand=True)


# destination input
destination_label = ttk.Label(input_frame, text="Zielort: ")
destination_label.pack(fill="x", expand=True)

destination_input = ttk.Entry(input_frame, textvariable=destination_value)
destination_input.pack(fill="x", expand=True)

# submit button
ttk.Button(input_frame, text="berechnen", command=submit_click).pack()


root.mainloop()
