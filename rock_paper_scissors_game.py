import random
rock = "🪨"
paper = "📃"
scissors = "✂️"
game_image = [rock, paper, scissors]

user_choice = int(input("Choose 0 rock, 1 paper, 2 scissors: "))

if user_choice < 0 or user_choice > 2:
    print("Invalid Choice")
else:
    print("\n You chose ")
    print(game_image[user_choice])

    computer_choice = random.randint(0,2)
    print("\n Computer chose ")
    print(game_image[computer_choice])

    if user_choice == computer_choice:
        print("\n It's a tie")
    elif user_choice == 0 and computer_choice == 2:
        print("\n You win")
    elif user_choice == 2 and computer_choice == 0:
        print("\n You lose")
    elif user_choice > computer_choice:
        print("\n You win")
    else:
        print("\n You lose")