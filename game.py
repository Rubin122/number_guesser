import random

print("Welcome to my number guessing game! Choose which range of numbers you want to guess from and I will say if it is either greater or less than the correct number. Keep Guessing until you get it right! I will also keep track of how many wins you get.")
     
total_wins = 0

while True:
    activation = input("Start game? y/n: ").lower()
    if activation not in ("y", "n"):
        print("Choose y or n only!")
        continue

    if activation == "n":
        print("Type y to start the game when ready.")
        continue

    print("Choose which range of numbers you want to play:")
    print(" 1) 1-10")
    print(" 2) 1-100")
    print(" 3) 1-1000")
    mode = input("Select 1, 2 or 3: ").strip()

    if mode == "1":
        upper = 10
    elif mode == "2":
        upper = 100
    elif mode == "3":
        upper = 1000
    else:
        print("Choose 1, 2 or 3!")
        continue

    correct_number = random.randint(1, upper)
    
    while True:
        try:

            player_guess = int(input(f"Guess a number from 1 to {upper}: "))

            if not (1 <= player_guess <= upper):
                print(f"Your guess must be a whole number between 1 and {upper}!")
                continue
        
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if player_guess == correct_number:
            print("You got it correct!")
            total_wins += 1
            print(f"You now have a total of {total_wins} total wins!")
            break
        elif player_guess > correct_number:
            print(f"{player_guess} is greater than the correct number")
            
        else:
            print(f"{player_guess} is less than the correct number")

    retry = input("Would you like to play again? y/n: ").lower()

    if retry not in ("y", "n"):
        print("Choose y or n only!")
        continue
    if retry == "n":
        print(f"You got {total_wins} total wins. Thanks for playing!")
        break
        



