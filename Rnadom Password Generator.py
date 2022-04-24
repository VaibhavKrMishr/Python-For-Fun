import random

while True:

    lower = ("abcdefghijklmnopqrstuvxxyz")
    upper = lower.upper()
    
    number = ("1234567890")
    
    symbol = ("@#$%*()_.{}")
    
    lenght = 9
    
    all = lower+upper+number+symbol
    
    password = "".join(random.sample(all,lenght))
    
    print(f"\nYour Password Is : {password}")
    
    generate_again =  input("Generate Again? (Y/N):")
    possible_outcomes =  ['y', 'n','yes', 'no']
    if   generate_again.lower() not in possible_outcomes:
        print ("Enter Vaild Input")
        break 
