'''Juggler Sequence, by Daniel Joseph T. Castro mail.datajunkie@gmail.com
Display the numbers in the juggler sequence series, the number of steps
before reaching 1, the maximum value in the series, and the sum of the
numbers in the series.
More info on https://en.wikipedia.org/wiki/Juggler_sequence
Tags: short, math, number series'''

from math import sqrt, trunc


def juggler_sequence(num):
    '''Returns a list of numbers in the
    juggler sequence series'''
    juggler_seq = []
    # Appends the first term of the series
    juggler_seq.append(num)
    while num != 1:
        # While the number in the next term
        # is not 1, this loop will continue to
        # calculate a new value and then appends
        # into the juggler_seq list.
        if num % 2 == 0:
            num = trunc(sqrt(num))
        else:
            num = trunc(sqrt(num ** 3))
        juggler_seq.append(num)
    else:
        return juggler_seq


def main():
    print('''\tJuggler Sequence by Daniel Joseph T. Castro 
    mail.datajunkie@gmail.com

    Juggler sequence is a number sequence that starts with
    a positive integer, a(n) with each subsequent term in the
    sequence is defined by the recurrence relation:

    a(n + 1) = \u221Aa\u0305(n), if a(n) is even
    a(n + 1) = \u221Aa\u0305(n)\u00B3, if a(n) is odd''')
    print("\n")
    # Asks the user to input a first-term number
    n = int(input("Enter a first-term number(Enter 0 to quit): "))

    while n != 0:
        # As long as the user does not enter 0, the program will
        # ask to the user for another first-term number.
        output = juggler_sequence(n)
        print(f"The numbers in the juggler sequence series with n = {n} are:")
        for i in range(len(output)):
            if 0 <= i < len(output) - 1:
                print(output[i], end="")
                print(",", end=" ")
            elif i == len(output) - 1:
                print(output[i], end="")

        print("\n")
        print(f"Number of steps to reach 1: {len(output) - 1}")
        print(f"Maximum value in the series: {max(output)}")
        print(f"Sum of al the numbers in the series: {sum(output)}")
        print("\n")
        n = int(input("Enter a first-term number(Enter 0 to quit): "))


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()


