import random
options=["rock", "paper", "scissors", "q"]
while True:
    user_input=input("Enter rock, paper, scissors or q to quit: ").lower()
    if user_input=="q":
        print("Thanks for playing")
        break
    if user_input not in options:
        print("invalid input")
        continue
    computer_options=["rock", "paper", "scissors"]
    computer_pick = random.choice(computer_options)
    print(f"computer picked: {computer_pick}")
    if (user_input=="rock" and computer_pick=="scissors") or (user_input=="paper" and computer_pick=="rock") or (user_input=="scissors" and computer_pick=="paper"):
        print("You Won!")
    elif user_input==computer_pick:
        print("tie")
    else:
        print("you lose")