import random
while True:
    print("ROCK, PAPER, SCISSOR GAME")
    user_action = input("Enter Your Option(Rock, Paper, Scissor):")
    possible_actions = ['rock', 'paper','scissor']
    computer_action = random.choice(possible_actions)


    if user_action.lower() not in possible_actions:  
        print ("Enter Vaild Input")
        
        break

    
    print (f"\nYour choice: {user_action} AND Computer choice: {computer_action} \n" )

    
    if user_action.lower() == computer_action:
        print (f"\nBoth Player Selected {user_action}. It's a Tie! \n")
    
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
             
    play_again =  input("Play Again? (Y/N):")
    possible_outcomes =  ['y', 'n','yes', 'no']
    if   play_again.lower() not in possible_outcomes:
        print ("Enter Vaild Input")
        break 

        
        break
    
