import random

def my_function():
    
        lower = ("abcdefghijklmnopqrstuvxxyz")
        upper = lower.upper()
    
        number = ("1234567890")
    
        symbol = ("@#$%*()_.{}")
    
        lenght = int(input("Enter The Length of Your Password:"))
    
        all_ = lower+upper+number+symbol
    
        password = "".join(random.sample(all_,lenght))

        return password

file = open("Passwords_collector.txt","a+")
key = input("Enter Key:")
passcode = my_function()

print(f"\n{key} : {passcode}")
input("Press Enter To Save.")

file.write(f"\n{key}:{passcode}\n")

file.close()
