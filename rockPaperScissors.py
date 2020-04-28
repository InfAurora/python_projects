import sys
import random
win = 0
lose = 0
tie = 0
def main():
    play = True
    while play:
        numRounds = input("How many rounds do you want to play? ")
        numRounds = int(numRounds)
        if numRounds > 10 or numRounds < 1:
            print("You must enter in a number between 1 and 10.")
            sys.exit()
        else:
            for i in range(numRounds):
                roundNum = i + 1
                guess = input("1. Rock\n2. Paper\n3. Scissors\n")
                guess = int(guess)
                if guess > 3 or guess < 1:
                    print("You must enter in a guess of 1, 2, or 3.")
                    sys.exit()
                outcome(guess)
        stats(win, lose, tie)
        again = input("Do you want to play again?\n1. Yes\n2. No\n")
        again = int(again)
        if again > 2 or again < 1:
            print("That is not a valid answer, goodbye!")
            sys.exit()
        if again == 2:
            play = False
            print("Thank you for playing! Goodbye!")
            return play
    
def outcome(guess):
    rChoice = random.choice([1, 2, 3])
    if (rChoice == 1 and guess == 1) or (rChoice == 2 and guess == 2) or (rChoice == 3 and guess == 3):
        print("Tie!")
        global tie 
        tie += 1
    elif (rChoice == 1 and guess == 3) or (rChoice == 2 and guess == 1) or (rChoice == 3 and guess == 2):
        print("You win!")
        global win
        win += 1
    else:
        print("You lose!")
        global lose
        lose += 1

def stats(win, lose, tie):
    if win > lose:
        print("You have won more rounds then me! Good job!")
    elif lose > win:
        print("You have lost more then me. Sorry!")
    else:
        print("We have tied in wins and losses!")
    print(f"Wins: {win}\nLosses: {lose}\nTies: {tie}")

if __name__ == "__main__":
    main()