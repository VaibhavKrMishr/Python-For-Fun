import random
while True:
    print("Coin Toss Program")
    
    user_action = input("Enter Your Choice(Head or Tail):")
    
    possible_actions = ('head','tail')
    
    computer_action = random.choice(possible_actions)
    
    if user_action.lower() not in possible_actions:  
        print ("Enter Vaild Input")
        
        break

    
    if user_action.lower() == computer_action:
        print(f"\nIt's {user_action}. You Won!")

        
        
    else:
        print(f"\nIt's {computer_action}. You lose!")


             
    play_again =  input("Play Again? (Y/N):")
    if play_again.upper() == "N":


        
        break
    

    
    
