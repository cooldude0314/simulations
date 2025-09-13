import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import seaborn as sns
import coinflip.coinflip
from coinflip.coinflip import CoinFlipSim
from dicerolls.dicerolls import DiceRollSim

class SimApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cool Dude Simulations Inc.")

        self.data = {} # dictionary to hang data results off
        self.sims = {}

        # Configure style
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        self.setup_ui()

    def setup_ui(self):
        # Create main frame
        control_frame = ttk.Frame(self, padding="10")
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

               # Control Panel
        self.setup_controls(control_frame)

    def setup_controls(self, frame):
        # Tabs for different simulations
        tab_control = ttk.Notebook(frame)
        tab_control.pack(side=tk.TOP, fill=tk.X)

        # Coin Flip Tab
        coin_flip_tab = ttk.Frame(tab_control)
        tab_control.add(coin_flip_tab, text="Coin Flip")
        self.sims['coin_flip'] = CoinFlipSim(coin_flip_tab)

        # Dice Rolls Tab 
        dice_roll_tab = ttk.Frame(tab_control)
        tab_control.add(dice_roll_tab, text="Dice Rolls")
        self.sims['dice_rolls'] = DiceRollSim(dice_roll_tab)



def main():
    res_x = 1200
    res_y = 800
    root = SimApp()

    # Center window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (res_x // 2)
    y = (root.winfo_screenheight() // 2) - (res_y // 2)
    root.geometry(f"{res_x}x{res_y}+{x}+{y}")

    root.mainloop()


if __name__ == "__main__":
    main()

