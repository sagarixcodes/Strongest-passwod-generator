import random

print("***WELCOME to our Guess the number Game!***\n")
print("Rules:\n1)don't change is code to Win.\n2)NO rules to display.\n3)Rules are over.\n ")
print("Instructions:\n1)Guess the number.\n2)If game shows Guessed no. < Generator no. ,this means that your number is smaller than Genrater number.\n3)If game shows Guessed no. > Generator no. ,this means that your number is greater than Genrater number.\n4)the range of number is between 0 and 100\n")
print("Good Luck")
print("Press Enter key to start game....")
input()
print("Number is generated..")

Generated_number = random.randint(1,100)

i = 1
while True:
    user_number = int(input(f"Attempt {i} : "))
    if user_number == Generated_number:
        print(f"You Won you gessed the generated number '{Generated_number}' in '{i}' Attempts.")
        score = 100 - i
        print("your score is : * {score} * ")
        break
    i += 1
    if user_number > Generated_number:
        print(f"Result  {i-1} : Guessed no. > Generator no.")
        continue    
            
    if user_number < Generated_number:
        print(f"Result  {i-1} : Guessed no. < Generator no.") 
        continue   

           

    





