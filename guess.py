# Guess the middle of a range of numbers, returning how many guesses it took
def guess(left, right):

    # Check base case, there's only one number left to guess
    if left == right:
        print("Your number is {}.".format(right))
        return 1

    mid = int(left + (right - left)/2)

    # If element is present at the middle itself 
    hint = input(str(mid) + '?')
    if (hint == 'h'):
        return 1 + guess(left, mid - 1)
    elif (hint == 'l'):
        return 1 + guess(mid + 1, right)
    else:
        return guess(mid, mid)

# Main game loop
def guessing_game():
    times = 0
    total = 0
    playing = True
    
    print("In this game, you think of a number from 1 through n and I will try to guess\n what it is. After each guess, enter h if my guess is too high, l if too low,\nor c if correct.\n")
    max = int(input("Please enter a number n: "))

    while playing:
        guesses = guess(1, max)
        print("It took me {} guesses.".format(guesses))
        
        total += guesses
        times += 1
        print("I averaged {} guesses per game for {} game(s).".format(total / times, times))
        
        choice = input("Play again (y/n)?")
        if (choice != 'y' and choice != 'Y'):
            playing = False

# And go!
guessing_game()