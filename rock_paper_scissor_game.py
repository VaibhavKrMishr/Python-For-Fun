import random

print("ROCK, PAPER, SCISSOR GAME\n")
possible_actions = ['rock', 'paper', 'scissor']

while True:
    user_action = input("Enter Your Option (Rock, Paper, Scissor): ")
    computer_action = random.choice(possible_actions)

    if user_action.lower() not in possible_actions:  
        print ("Enter Vaild Input")
        continue
    
    print (f"\nYour choice: {user_action.title()} AND Computer choice: {computer_action.title()}\n" )
    
    if user_action.lower() == computer_action:
        print (f"Both Players Selected {user_action.title()}. It's a Tie! \n")
    
    elif user_action.lower() == "rock":
         if computer_action == "scissor":
             print("You Win!")
         else:
             print("You Lose")
         
    elif user_action.lower() == "scissor":
         if computer_action == "paper":
             print("You Win!")
         else:
             print("You Lose")
         
    elif user_action.lower() == "paper":
         if computer_action == "rock":
             print("You Win!")
         else:
             print("You Lose")
             
    play_again =  input("Play Again? (Y/N):") + " "

    if play_again[0].lower() == 'n':
        break