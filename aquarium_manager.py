# aquarium_manager.py

import tkinter as tk
from aquarium_gui import AquariumGUI

def main():
    root = tk.Tk()
    app = AquariumGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
