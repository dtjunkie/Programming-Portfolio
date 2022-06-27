from random import sample
from time import sleep

def auto_pick():
    pick = sample(range(1,43),6)
    return pick

def compare_pick(pick_1, pick_2):
    n = 0
    for num in pick_1:
        if num in pick_2:
            n += 1
    return n

def main():
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

if __name__ == '__main__':
    main()
