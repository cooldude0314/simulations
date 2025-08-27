import random

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def generate_roll_data(num_rolls, sides):
    roll_data = []
    for _ in range(num_rolls):
        dice_1 = random.randint(1, sides)
        dice_2 = random.randint(1, sides)
        total = dice_1 + dice_2
        roll_data.append((dice_1, dice_2, total))
    return roll_data

class DiceRollSim:
    def __init__(self, tab):
        self.tab = tab
        self.setup_tab(tab)
    
    def setup_tab(self, tab):
        self.num_rolls_label = ttk.Label(tab, text="Number of Rolls:")
        self.num_rolls_label.grid(column=0, row=0, sticky=tk.W)

        self.num_rolls_entry = ttk.Entry(tab)
        self.num_rolls_entry.grid(column=1, row=0)

        self.sides_label = ttk.Label(tab, text="Number of Sides:")
        self.sides_label.grid(column=0, row=1, sticky=tk.W)

        self.sides_entry = ttk.Entry(tab)
        self.sides_entry.grid(column=1, row=1)

        self.roll_button = ttk.Button(tab, text="Roll Dice", command=self.roll_dice)
        self.roll_button.grid(column=0, row=2, columnspan=2)

    def roll_dice(self):
        num_rolls = int(self.num_rolls_entry.get())
        sides = int(self.sides_entry.get())
        self.data = generate_roll_data(num_rolls, sides)
        self.render_results()

    def render_results(self):
        print("render")
        # draw matplot histogram of dice totals
        if not self.data:
            return

        totals = [total for _, _, total in self.data]
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot()
        ax.hist(totals)
        print("hi")
        ax.set_title("Dice Roll Totals")
        ax.set_xlabel("Total")
        ax.set_ylabel("Frequency")
        #plt.hist(totals, bins=range(2, 2 * (int(self.sides_entry.get()) + 1)), edgecolor='black')
        #+sns.histplot(totals, bins=range(2, 2 * (int(self.sides_entry.get()) + 1)), kde=False
                     #).set(title="Dice Roll Totals", xlabel="Total", ylabel="Frequency")
        canvas = FigureCanvasTkAgg(fig, master=self.tab)  # A tk.DrawingArea.
        canvas.get_tk_widget().grid(row=1, column=0)
        canvas.draw()
        print("drawn")

#sides = int(input("How many sides? "))
#running = True
#while running:
#    def generate_roll_data(num_rolls, sides):
#        roll_data = []
#        for _ in range(num_rolls):
#            dice_1 = random.randint(1, sides)
#            dice_2 = random.randint(1, sides)
#            total = dice_1 + dice_2
#            prob = probability_of_total(total, sides)
#            print(f"Dice 1: {dice_1}, Dice 2: {dice_2}, Total: {total}")
#            print(f"Probability of rolling a total of {total}: {prob:.2%}")
#            roll_data.append((dice_1, dice_2, total))
#        return roll_data
#    def probability_of_total(n, sides=sides):
#        if n < 2 or n > 2 * sides:
#            return 0
#        combinations = min(n - 1, 2 * sides + 1 - n)
#        return combinations / (sides * sides)
#
#    num_rolls = int(input("Enter the number of rolls: "))
#
#        
    
#    data = generate_roll_data(num_rolls, sides)
#
#    cont = input("Press enter to roll again, type 'exit' to stop: ").strip().lower()
#    if cont == 'exit':
#        running = False
#print("Rolling complete.")
#for roll in data:
#    print(roll)