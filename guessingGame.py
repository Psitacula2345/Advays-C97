import random 
print ("number guessing game")
#randint-function to generate random number between 1-9
num = random.randint (1,9)
chances = 0
print ("guess a number between 1-9")
while chances < 5: 
    guess = int(input("enter your guess:"))
    if guess == num:
        print("you won")
        break 
    elif guess < num:
            print ("guess a number")
            chances = chances + 1
    if not chances < 5: 
        print ("you lose") 



