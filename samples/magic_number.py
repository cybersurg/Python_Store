secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
# Read the number entered

number = int(input("Enter a number or type 0 to stop: "))

while number != 0:
    
    if number != secret_number:
        
        print("Ha ha! You're stuck in my loop!")
        
        number = int(input("Enter a number or type 0 to stop: "))
        
    else:
        print("Well done, muggle! You are free now.")
        break
else:
    print("You chose to stop the game.")           
        

