'''LOTTO GAME, by Daniel Joseph T. Castro mail.datajunkie@gmail.com
A simulation game of the 6/42 Philippine Lotto Draw.
Tag: medium, game, simulation'''

from random import sample
from time import sleep

def auto_pick():
    '''Randomly draws 6 numbers from 1 to 42'''
    pick = sample(range(1,43),6)
    return pick

def compare_pick(pick_1, pick_2):
    '''Compares the computer-drawn numbers with
    the numbers picked by the user and returns
    the number of matches'''
    n = 0
    for num in pick_1:
        if num in pick_2:
            n += 1
    return n

def main():
    #Displays the intro
    print('''\tLOTTO GAME, by Daniel Joseph T. Castro mail.datajunkie@gmail.com\n
    INSTRUCTIONS: Pick 6 numbers from 1 to 42. Then, the computer will draw six
    numbers from 1 to 42 and then compares the numbers drawn by the computer 
    with the numbers that you picked. The user will win prizes depending on the
    number of matched numbers that you have.You will only get a prize if you will
    get 3 to 6 matching numbers in any order.\n
    NOTE: This is just a simulation game. No real money involved.\n''')

    while True:     #Main game loop
        # The user will pick 6 numbers from 1 to 42 and stores it to
        # a list. Should the user enter a number that was already picked
        # or entered a number beyond the range of 1 to 42, an error message
        # will be displayed and asks the user to enter another number.
        user_pick = []
        counter = 0
        user_input = int(input("Enter a number (1 to 42): "))
        user_pick.append(user_input)
        counter += 1
        while counter != 6:
            user_input = int(input("Enter another number (1 to 42): "))
            if user_input in user_pick:
                print("Number should not be repeated. Try Again.")
            elif user_input < 1 or user_input > 42:
                print("Number should be between 1 and 42. Try Again.")
            else:
                user_pick.append(user_input)
                counter += 1
        print("\r")
        # The computer will draw 6 random numbers from 1 to 42. Each number
        # will drawn in 5 seconds then displays it on screen.
        draw = auto_pick()
        print("The first number will be drawn in 5 seconds...", end="")
        sleep(5)
        for i in range(len(draw)):
            if i == 0:
                print(f"The first number is {draw[i]}.")
                print("The next number will be drawn in 5 seconds...", end="")
                sleep(5)
            elif 0 < i < 4:
                print(f"The next number is {draw[i]}.")
                print("The next number will be drawn in 5 seconds...", end="")
                sleep(5)
            elif i == 4:
                print(f"The next number is {draw[i]}.")
                print("The last number will be drawn in 5 seconds...", end="")
                sleep(5)
            elif i == 5:
                print(f"The last number is {draw[i]}.")
        print("\r")
        # Prints and displays the user picked numbers and the
        # computer-drawn numbers:
        print("You picked the numbers: ", end="")
        for i in range(len(user_pick)):
            if 0 <= i < 5:
                print(user_pick[i], end="")
                print(", ", end="")
            else:
                print(user_pick[i])
        print("Computer picked the numbers: ", end="")
        for i in range(len(draw)):
            if 0 <= i < 5:
                print(draw[i], end="")
                print(", ", end="")
            else:
                print(draw[i])
        # Then, the computer will compare the two sets of numbers
        # and returns a message based on the number of matched numbers.
        match = compare_pick(user_pick,draw)
        jackpot_prize = "10,518,111.40"
        prize_2nd = "24,000"
        prize_3rd = "800"
        prize_4th = "20"
        less_than_3 = "0"
        if match == 6:
            print(f"You've got {match} out of 6 drawn numbers. You've won \u20B1{jackpot_prize}. Congratulations!")
        elif match == 5:
            print(f"You've got {match} out of 6 drawn numbers. You've won \u20B1{prize_2nd}. Congratulations!")
        elif match == 4:
            print(f"You've got {match} out of 6 drawn numbers. You've won \u20B1{prize_3rd}. Congratulations!")
        elif match == 3:
            print(f"You've got {match} out of 6 drawn numbers. You've won \u20B1{prize_4th}. Congratulations!")
        elif match < 3:
            print(f"You've got {match} out of 6 drawn numbers. You've won \u20B1{less_than_3}. Better luck next time.")
        print("\r")
        # Asks the user if he/she wants to play again. If the user types
        # "N", the game will stop. Else it will restart the game.
        play_again = input("Do you want to play again? [Y/N]: ")
        if play_again == "N":
            break
    # Displays the message after the user enters "N":
    print("Thanks for playing Lotto Game!")

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
