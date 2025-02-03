import random
from art import logo

#number_of_lives() is used here to choose the difficulty by typing in 1,2 or 3, where 1= 2 lives, 2= 5 lives and 3 = 10 lives
def number_of_lives():
    while True:
        life = int(input("Choose a difficulty:\n'1' if you are a god\n'2' if you're up for a challange\n'3' if you like mango\n"))

        if life == 1:
            return 2
        elif life == 2:
            return 5
        elif life == 3:
            return 10
        else:
            print("TYPE ONE OF THE THREE NUMBERS DUDE CMON 🤦‍♂️")

#distance() calculates the diffrence between the user's guess and the actual number and tells the user how close they are to the actual number
def distance(num, guess):
    difference = num - guess

    if difference >= 10:
        return "Too Low"
    elif difference <= -10:
        return "Too High"
    elif 0< difference <10:
        return "Low"
    elif -10< difference <0:
        return "High"
    elif difference == 0:
        return "YOU GUESSED IT 👏👏👏👏 !!"

rerun = True

#This final loop works by iterating until the user either loses or wins
while True:

    #This checks if this is a rerun or 1st run and if it is then it'll assign the variables their values
    if rerun:
        print(logo + "\n"*3)
        num = random.randint(0, 100)
        life = number_of_lives()

        #This makes sure that rerun is false and the game doesnt reset after every iteration
        rerun = False

    print("Guess the number between 1 and 100")
    print(f"Lives remaining: {life}")
    guess = int(input("\nYour Guess: "))

    result = distance(num, guess)
    print( "\n"*5 + result)

    life -= 1

    if (num-guess) == 0 or life ==0:
        if life > 0:
            print("Congrats!!")
        else:
            print("OOPS!! You ran out of lives !")
            print(f"The correct number was {num}")

        rerun = int(input("Do you want to play again?'1' for yes, '2' for no:\n"))

        if rerun == 1:
            rerun = True
        elif rerun == 2:
            break
    