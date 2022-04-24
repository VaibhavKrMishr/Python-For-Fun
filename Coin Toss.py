import random


print("Welcome to my Coin Toss Program\nAuthor: VaibhavKrMishr\n")
# possible_actions = ('head', 'tail')

# new possible_actions
possible_actions = {
    1: "head",
    2: "tail",
}

run = True
while run:

    user_action = input("Enter Your Choice (Head or Tail) or (1 or 2): ")

    # converts 1 or 2 to head or tail
    if user_action.isdigit():
        if int(user_action) in possible_actions.keys():
            user_action = possible_actions[int(user_action)]
        else:
            print("Enter Vaild Input (Head or Tail) or (1 or 2)!")
            continue

    if user_action.lower() not in possible_actions.values():
        print("Enter Vaild Input (Head or Tail) or (1 or 2)!")
        continue
    
    computer_action = random.choice(list(possible_actions.values()))
    
    if user_action.lower() == computer_action:
        print(f"\nIt's {user_action.title()}. You Won!")
    else:
        print(f"\nIt's {computer_action.title()}. You lose!")

    play_again = input("\nPlay Again? (Y/N): ") + " "

    if play_again[0].lower() == "n":
        run = False