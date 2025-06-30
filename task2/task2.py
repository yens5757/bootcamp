import random


def generate_number():
    # this is for generating a number between 1 and 100
    return random.randint(1, 100)

def user_guess(low, high):
    # The program will ask for a user input. The user is required to type in a input that is within the current range.
    # And if the user didn't enter a valid input, the program will continue asking for input til the input is valid
    while True:
        guess = input(f"guess a number between {low} and {high}: ")
        # checks if guess is a valid input
        if not guess.isdigit():
            print(f"please enter a number from {low} to {high}")
            continue
        guess = int(guess)
        # checks if guess is in the range
        if guess < low or guess > high:
            print(f"please enter a number within {low} to {high}")
            continue
        else:
            return guess
        
def check_guess(ans, guess, low, high):
    # check the user guess to see if it's correct, should be higher, or should be lower
    if guess > ans:
        print("Lower!")
        return low, guess
    elif guess < ans:
        print("Higher!")
        return guess, high
    else:
        return ans, ans

def game_over(tries):
    # printing the winner message
    print(f"You win! You got it in {tries} tries!")

def main():
    # we first generate the random number as well as setting the range
    ans = generate_number()
    low, high = 1, 100
    tries = 0
    # we keep looping through this until user gets the correct answer.
    while True:
        tries += 1
        guess = user_guess(low, high)
        low, high = check_guess(ans, guess, low, high)
        if low == high:
            break
    game_over(tries)
    

main()