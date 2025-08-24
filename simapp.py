import random
import tkinter as tk
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import seaborn as sns
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

def generate_coin_flip_data(num_flips):
    return [1,2,3]

class SimApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cool Dude Simulations Inc.")

        self.data = {} # dictionary to hang data results off
        self.sim_tabs = {}

        # Configure style
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        self.setup_ui()

    def setup_ui(self):
        # Create main frame
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

               # Control Panel
        self.setup_controls(control_frame)
        self.setup_coin_flip_tab(self.sim_tabs['coin_flip'])

    def setup_controls(self, frame):
        # Tabs for different simulations
        tab_control = ttk.Notebook(frame)
        tab_control.pack(side=tk.TOP, fill=tk.X)

        # Coin Flip Tab
        coin_flip_tab = ttk.Frame(tab_control)
        tab_control.add(coin_flip_tab, text="Coin Flip")
        self.sim_tabs['coin_flip'] = coin_flip_tab

        # Dice Roll Tab
        dice_roll_tab = ttk.Frame(tab_control)
        tab_control.add(dice_roll_tab, text="Dice Roll")
        self.sim_tabs['dice_roll'] = dice_roll_tab

    def setup_coin_flip_tab(self, tab):
        # Coin Flip Simulation UI
        ttk.Label(tab, text="Coin Flip Simulation").pack(pady=10)
        # Input for number of flips
        ttk.Label(tab, text="Number of Flips:").pack(pady=5)
        self.num_flips_entry = ttk.Entry(tab)
        self.num_flips_entry.pack(pady=5)

        def run_coin_flip_simulation():
            num_flips = int(self.num_flips_entry.get())
            flip_data = generate_coin_flip_data(num_flips)
            self.data['coin_flip'] = flip_data

        ttk.Button(tab, text="Run Simulation", command=run_coin_flip_simulation).pack(pady=5)


def main():
    root = tk.Tk()
    _ = SimApp(root)

    res_x = 1200
    res_y = 800

    # Center window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (res_x // 2)
    y = (root.winfo_screenheight() // 2) - (res_y // 2)
    root.geometry(f"{res_x}x{res_y}+{x}+{y}")

    root.mainloop()

if __name__ == "__main__":
    main()

