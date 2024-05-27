# aquarium_gui.py

import tkinter as tk
from tkinter import ttk, messagebox
from aquarium import Aquarium
from fish import Fish
from maintenance import MaintenanceAction

class AquariumGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Aquarium Manager")
        
        self.aquarium = Aquarium()
        self.aquarium.load_data()
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.create_main_page()
        self.create_maintenance_page()
        
    def create_main_page(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.main_frame, text="Aquarium Manager")
        self.label.pack(pady=10)
        
        self.species_label = tk.Label(self.main_frame, text="Species")
        self.species_label.pack()
        self.species_entry = tk.Entry(self.main_frame)
        self.species_entry.pack(pady=5)
        
        self.number_label = tk.Label(self.main_frame, text="Number of Fish")
        self.number_label.pack()
        self.number_entry = tk.Entry(self.main_frame)
        self.number_entry.pack(pady=5)
        
        self.add_fish_button = tk.Button(self.main_frame, text="Add Fish", command=self.add_fish)
        self.add_fish_button.pack(pady=10)
        
        self.show_fish_button = tk.Button(self.main_frame, text="Show Fish", command=self.show_fish)
        self.show_fish_button.pack(pady=10)
        
        self.fish_list_label = tk.Label(self.main_frame, text="")
        self.fish_list_label.pack(pady=10)

        self.maintenance_button = tk.Button(self.main_frame, text="Go to Maintenance", command=self.show_maintenance_page)
        self.maintenance_button.pack(pady=10)
        
    def create_maintenance_page(self):
        self.maintenance_frame = tk.Frame(self.master)
        
        self.action_label = tk.Label(self.maintenance_frame, text="Maintenance Action")
        self.action_label.pack()
        
        self.action_var = tk.StringVar()
        self.action_dropdown = ttk.Combobox(self.maintenance_frame, textvariable=self.action_var)
        self.action_dropdown['values'] = ("filter cleaning", "water change", "added fertilizer")
        self.action_dropdown.bind("<<ComboboxSelected>>", self.action_selected)
        self.action_dropdown.pack(pady=5)
        
        self.date_label = tk.Label(self.maintenance_frame, text="Date (YYYY-MM-DD)")
        self.date_label.pack()
        self.date_entry = tk.Entry(self.maintenance_frame)
        self.date_entry.pack(pady=5)
        
        self.time_label = tk.Label(self.maintenance_frame, text="Time (HH:MM)")
        self.time_label.pack()
        self.time_entry = tk.Entry(self.maintenance_frame)
        self.time_entry.pack(pady=5)
        
        self.quantity_label = tk.Label(self.maintenance_frame, text="Quantity (ml)")
        self.quantity_entry = tk.Entry(self.maintenance_frame)
        
        self.add_action_button = tk.Button(self.maintenance_frame, text="Add Maintenance Action", command=self.add_maintenance_action)
        self.add_action_button.pack(pady=10)
        
        self.show_log_button = tk.Button(self.maintenance_frame, text="Show Maintenance Log", command=self.show_maintenance_log)
        self.show_log_button.pack(pady=10)
        
        self.maintenance_log_label = tk.Label(self.maintenance_frame, text="")
        self.maintenance_log_label.pack(pady=10)
        
        self.back_button = tk.Button(self.maintenance_frame, text="Back to Main", command=self.show_main_page)
        self.back_button.pack(pady=10)

    def add_fish(self):
        species = self.species_entry.get()
        try:
            number = int(self.number_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for fish.")
            return
        
        if species and number > 0:
            new_fish = Fish(species, number)
            self.aquarium.add_fish(new_fish)
            messagebox.showinfo("Add Fish", f"Added {number} {species} fish to the aquarium.")
            self.species_entry.delete(0, tk.END)
            self.number_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Input Error", "Please enter valid species and number.")

    def show_fish(self):
        fish_list = self.aquarium.get_fish_list()
        if fish_list:
            self.fish_list_label.config(text="\n".join(fish_list))
        else:
            self.fish_list_label.config(text="No fish in the aquarium.")
            
    def action_selected(self, event):
        if self.action_var.get() == "added fertilizer":
            self.quantity_label.pack(pady=5)
            self.quantity_entry.pack(pady=5)
        else:
            self.quantity_label.pack_forget()
            self.quantity_entry.pack_forget()

    def add_maintenance_action(self):
        action = self.action_var.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        quantity = self.quantity_entry.get() if action == "added fertilizer" else None
        
        if action and date and time and (action != "added fertilizer" or quantity):
            new_action = MaintenanceAction(action, date, time, quantity)
            self.aquarium.add_maintenance_action(new_action)
            messagebox.showinfo("Maintenance Action", f"Added maintenance action: {new_action.get_info()}")
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Input Error", "Please fill in all required fields.")

    def show_maintenance_log(self):
        log = self.aquarium.get_maintenance_log()
        if log:
            self.maintenance_log_label.config(text="\n".join(log))
        else:
            self.maintenance_log_label.config(text="No maintenance actions recorded.")

    def show_main_page(self):
        self.maintenance_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    def show_maintenance_page(self):
        self.main_frame.pack_forget()
        self.maintenance_frame.pack(fill="both", expand=True)

    def on_closing(self):
        self.aquarium.save_data()
        self.master.destroy()
        
def main():
    root = tk.Tk()
    app = AquariumGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
