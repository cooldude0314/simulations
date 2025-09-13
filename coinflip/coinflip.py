import random
import tkinter as tk
from tkinter import ttk
import time
import matplotlib.pyplot as plt
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

def generate_coin_flip_data(num_flips):
    return [random.choice(["Heads", "Tails"]) for _ in range(num_flips)]

class CoinFlipSim:
    def __init__(self, tab):
        self.tab = tab
        self.setup_coin_flip_tab()
        self.data = None

    def setup_coin_flip_tab(self):
        tab = self.tab
        # Coin Flip Simulation UI
        ttk.Label(tab, text="Coin Flip Simulation").pack(pady=10)
        # Input for number of flips
        ttk.Label(tab, text="Number of Flips:").pack(pady=5)
        self.num_flips_entry = ttk.Entry(tab)
        self.num_flips_entry.pack(pady=5)

        def run_coin_flip_simulation():
            num_flips = int(self.num_flips_entry.get())
            flip_data = generate_coin_flip_data(num_flips)
            self.data = flip_data
            self.render_results()

        ttk.Button(tab, text="Run Simulation", command=run_coin_flip_simulation).pack(pady=5)

    def render_results(self):       
        if not self.data:
           return
        
        x = []
        y = []
        error = []
        heads_count = 0
        total_dev = 0
        for idx,data in enumerate(self.data):
            x.append(idx + 1)
            if data == "Heads":
                heads_count += 1
            heads_prob = float(heads_count)/(idx + 1)
            y.append(heads_prob)

            dev = (heads_prob - 0.5) ** 2
            total_dev += dev
            error.append(total_dev)

        # plt.plot(x, y)
        # plt.ylim(0, 1)
        # plt.show()
        plt.plot(x,error)
        plt.show()


#print("Starting up....")
#running = True
#while running:
#    def show_flip(side, root, canvas):
#        canvas.delete("all")
#        root.update()
#        time.sleep(0.1)# Pause for a brief moment so the user can see that the coin flips again if it lands on the same side
#        root.title("Coin Flip Result")
#
#        if side == "Heads":
#            # Draw a yellow circle for heads
#            canvas.create_oval(150, 150, 250, 250, fill="yellow")
#            canvas.create_text(100, 100, text="Heads", font=("Arial", 20))
#        else:
#            # Draw a gray circle for tails
#            canvas.create_oval(150, 150, 250, 250, fill="gray")
#            canvas.create_text(100, 100, text="Tails", font=("Arial", 20))
#        root.update()
#        time.sleep(1)  # Pause for a second to show the result
#    
#    time.sleep(2.5)
#    times = int(input("\nHow many times? "))
#    num_tails = 0
#    num_heads = 0
#    while times > 0:
#        flip = random.randint(1,2)
#        if flip == 1:
#            side = "Heads"
#            num_heads += 1
#        elif flip == 2:
#            side = "Tails"
#            num_tails += 1
#        print(side)
#        show_flip(side, root, canvas)
#        times -= 1
#    print("Heads:", num_heads)
#    print("Tails:", num_tails)
#    print("Percentage of Heads: {:.2%}".format(num_heads / (num_heads + num_tails)))
#    print("Percentage of Tails: {:.2%}".format(num_tails / (num_heads + num_tails)))
#    if num_heads > num_tails:
#        print("More heads!")
#    elif num_heads < num_tails:
#        print("More tails!")
#    elif num_heads == num_tails:
#        print("Same number of heads and tails!")
#    if input("Press enter to flip again or type 'exit' to stop: ").lower() == 'exit':
#        running = False
#        break
#root.mainloop()