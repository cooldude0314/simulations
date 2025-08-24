import random

sides = int(input("How many sides? "))
running = True
while running:
    def generate_roll_data(num_rolls, sides):
        roll_data = []
        for _ in range(num_rolls):
            dice_1 = random.randint(1, sides)
            dice_2 = random.randint(1, sides)
            total = dice_1 + dice_2
            prob = probability_of_total(total, sides)
            print(f"Dice 1: {dice_1}, Dice 2: {dice_2}, Total: {total}")
            print(f"Probability of rolling a total of {total}: {prob:.2%}")
            roll_data.append((dice_1, dice_2, total))
        return roll_data, total
    def probability_of_total(n, sides=sides):
        if n < 2 or n > 2 * sides:
            return 0
        combinations = min(n - 1, 2 * sides + 1 - n)
        return combinations / (sides * sides)

    num_rolls = int(input("Enter the number of rolls: "))

        
    
    data = generate_roll_data(num_rolls, sides)

    cont = input("Press enter to roll again, type 'exit' to stop: ").strip().lower()
    if cont == 'exit':
        running = False
print("Rolling complete.")
print(data) 